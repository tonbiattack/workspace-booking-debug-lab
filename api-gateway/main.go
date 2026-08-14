package main

import (
  "log"
  "net/http"
  "github.com/go-chi/chi/v5"
  "github.com/tonbiattack/workspace-booking-debug-lab/api-gateway/internal/gateway"
)
func main() {
  r := chi.NewRouter()
  r.Use(gateway.RequestID)
  r.Get("/api/availability", func(w http.ResponseWriter, r *http.Request) { w.Header().Set("Content-Type", "application/json"); _, _ = w.Write([]byte(`{"items":[]}`)) })
  r.Get("/health", func(w http.ResponseWriter, r *http.Request) { _, _ = w.Write([]byte("ok")) })
  log.Fatal(http.ListenAndServe(":8080", r))
}
