package gateway
import "testing"
func TestR01DownstreamFailureIsNotSuccess(t *testing.T) { if !PropagateDownstream(502) { t.Fatal("502 must be propagated") } }
func TestR10RequestIDIsForwarded(t *testing.T) { if ForwardRequestID("req-1") != "req-1" { t.Fatal("request id must be forwarded") } }
