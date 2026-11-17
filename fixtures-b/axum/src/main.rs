use axum::{extract::State, routing::get, Router};
use sqlx::postgres::{PgPool, PgPoolOptions};

#[derive(Clone)]
struct AppState {
    pool: PgPool,
}

async fn health(State(state): State<AppState>) -> &'static str {
    match sqlx::query("SELECT 1").execute(&state.pool).await {
        Ok(_) => "ok",
        Err(_) => "db down",
    }
}

#[tokio::main]
async fn main() {
    let url = std::env::var("DATABASE_URL").unwrap_or_else(|_| "postgres://localhost/users".into());
    let pool = PgPoolOptions::new().connect_lazy(&url).expect("bad DATABASE_URL");
    let app = Router::new()
        .route("/health", get(health))
        .with_state(AppState { pool });

    let listener = tokio::net::TcpListener::bind("0.0.0.0:3000").await.unwrap();
    axum::serve(listener, app).await.unwrap();
}
