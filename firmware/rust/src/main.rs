// Create Web API for my Raspberry Pi Gesture Recognition project

use actix_web::{get, web, App, HttpResponse, HttpServer, Responder, Result};
use actix_cors::Cors;
use serde::{Serialize};

#[derive(Serialize)]
pub struct Response {
    pub message: String,
}

#[get("/health")]
async fn healthcheck() -> impl Responder {
    let response = Response {
        message: "Everything is working fine".to_string(),
    };
    HttpResponse::Ok().json(response)
}


async fn not_found() -> Result<HttpResponse> {
    let response = Response {
        message: "Resource not found".to_string(),
    };
    Ok(HttpResponse::NotFound().json(response))
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    // Allow CORS
   
        HttpServer::new(move || {
            let cors = Cors::default()
                .allow_any_origin()
                .allow_any_method()
                .allow_any_header();
    
            App::new()
                .wrap(cors)
                .service(healthcheck)
                .default_service(web::route().to(not_found))
        })
        .bind(("127.0.0.1", 8084))?
        .run()
        .await
    
}