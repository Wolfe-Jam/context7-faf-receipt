package main

import (
	"encoding/json"
	"log"
	"net/http"
	"sync"
)

type User struct {
	ID    int    `json:"id"`
	Name  string `json:"name"`
	Email string `json:"email"`
}

type store struct {
	mu    sync.RWMutex
	users map[int]User
}

func newStore() *store {
	return &store{users: map[int]User{1: {ID: 1, Name: "Ada", Email: "ada@example.com"}}}
}

func writeJSON(w http.ResponseWriter, status int, v any) {
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(status)
	json.NewEncoder(w).Encode(v)
}

func main() {
	s := newStore()
	mux := http.NewServeMux()
	mux.HandleFunc("GET /health", func(w http.ResponseWriter, r *http.Request) {
		writeJSON(w, http.StatusOK, map[string]bool{"ok": true})
	})
	_ = s
	log.Fatal(http.ListenAndServe(":8080", mux))
}
