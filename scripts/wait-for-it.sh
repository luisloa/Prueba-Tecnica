set -e

host="$1"
shift
port="$1"
shift

timeout=15
quiet=0

while [[ "$1" != "--" ]]; do
  case "$1" in
    -q | --quiet)
      quiet=1
      shift
      ;;
    -t | --timeout)
      timeout="$2"
      shift 2
      ;;
    *)
      echo "Unknown option: $1"
      exit 1
      ;;
  esac
done

shift

start_time=$(date +%s)
end_time=$((start_time + timeout))

while :
do
  if nc -z "$host" "$port"; then
    break
  fi
  now=$(date +%s)
  if [ "$now" -ge "$end_time" ]; then
    echo "Timeout after $timeout seconds waiting for $host:$port"
    exit 1
  fi
  [ "$quiet" -ne 1 ] && echo "⏳ Esperando a que $host:$port esté disponible..."
  sleep 1
done

[ "$quiet" -ne 1 ] && echo "✅ $host:$port está disponible, iniciando aplicación..."
exec "$@"