// Create Web API for my Raspberry Pi Gesture Recognition project

use actix_cors::Cors;
use actix_web::{get, web, App, HttpResponse, HttpServer, Responder, Result};
use log::{debug, error};
use serde::Serialize;
use simplelog::{CombinedLogger, TermLogger, WriteLogger};
use std::fs::File;

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

#[get("/start_gesture_recognition")]
async fn start_gesture_recognition() -> impl Responder {
    // Call the gesture recognition script
    let output = std::process::Command::new("bash")
        .arg("../firmware/python/scripts/start.sh")
        .output()
        .expect("failed to execute process");

    // Check if the gesture recognition script was executed successfully
    if output.status.success() {
        debug!("Gesture Recognition Started");
    } else {
        error!("Gesture Recognition Failed");
    }

    // Print output of the gesture recognition script
    println!("stdout: {}", String::from_utf8_lossy(&output.stdout));

    let response = Response {
        message: "Gesture Recognition Started".to_string(),
    };
    HttpResponse::Ok().json(response)
}

#[get("/stop_gesture_recognition")]
async fn stop_gesture_recognition() -> impl Responder {
    // Call the gesture recognition script
    let output = std::process::Command::new("bash")
        .arg("../firmware/python/scripts/end.sh")
        .output()
        .expect("failed to execute process");

    // Check if the gesture recognition script was executed successfully
    if output.status.success() {
        debug!("Gesture Recognition Stopped");
    } else {
        error!("Gesture Recognition Failed");
    }

    let response = Response {
        message: "Gesture Recognition Stopped".to_string(),
    };
    HttpResponse::Ok().json(response)
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    /* Instantiate Logger */
    match CombinedLogger::init(vec![
        TermLogger::new(
            log::LevelFilter::Debug,
            simplelog::Config::default(),
            simplelog::TerminalMode::Mixed,
            simplelog::ColorChoice::Auto,
        ),
        WriteLogger::new(
            log::LevelFilter::Debug,
            simplelog::Config::default(),
            File::create("gesture_recognition.log").unwrap(),
        ),
    ]) {
        Ok(_) => debug!("Logger initialized"),
        Err(e) => debug!("Logger failed to initialize: {}", e),
    }
    HttpServer::new(move || {
        let cors = Cors::default()
            .allow_any_origin()
            .allow_any_method()
            .allow_any_header();

        App::new()
            .wrap(cors)
            .service(healthcheck)
            .service(start_gesture_recognition)
            .service(stop_gesture_recognition)
            .default_service(web::route().to(not_found))
    })
    .bind(("192.168.0.161", 8080))?
    .run()
    .await
}
