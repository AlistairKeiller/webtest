use actix_web::{get, web, App, HttpResponse, HttpServer, Responder};
use reqwest::Client;

#[get("/")]
async fn index() -> impl Responder {
    "Hello, World!"
}

#[get("/{d}")]
async fn forward(d: web::Path<String>) -> HttpResponse {
    let client = Client::new();
    let forward_url = format!("https://use.typekit.net/{}", d);

    let response = client.get(&forward_url).send().await;

    match response {
        Ok(resp) => {
            let status = resp.status();
            let content_type = resp
                .headers()
                .get(reqwest::header::CONTENT_TYPE)
                .map_or_else(|| "text/plain", |v| v.to_str().unwrap_or("text/plain"))
                .to_string(); // Clone the content type here

            if status.is_success() {
                match resp.bytes().await {
                    Ok(bytes) => {
                        HttpResponse::Ok()
                            .content_type(content_type) // Pass cloned content type directly
                            .body(bytes)
                    }
                    Err(_) => HttpResponse::InternalServerError().finish(),
                }
            } else {
                HttpResponse::BadRequest().finish()
            }
        }
        Err(_) => HttpResponse::InternalServerError().finish(),
    }
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| App::new().service(index).service(forward))
        .bind(("127.0.0.1", 8080))?
        .run()
        .await
}
