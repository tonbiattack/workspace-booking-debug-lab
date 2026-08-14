package gateway
import ( "context"; "fmt"; "net/http"; "time" )
type contextKey string
const requestIDKey contextKey = "requestId"
func RequestID(next http.Handler) http.Handler { return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) { id := r.Header.Get("X-Request-Id"); if id == "" { id = fmt.Sprintf("req-%d", time.Now().UnixNano()) }; started := time.Now(); w.Header().Set("X-Request-Id", id); next.ServeHTTP(w, r.WithContext(context.WithValue(r.Context(), requestIDKey, id))); _ = started }) }
func PropagateDownstream(status int) bool { return status >= 400 }
func ForwardRequestID(id string) string { return "" }
