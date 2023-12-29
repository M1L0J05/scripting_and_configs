#! /bin/bash

# small template for my bash shell scripts.

set -o errexit  # the script ends if a command fails
set -o pipefail # the script ends if a command fails in a pipe
set -o nounset  # the script ends if it uses an undeclared variable
#set -o xtrace # if you want to debug


# Log functions
error() {
  printf "\033[0;31m%s\033[0m\n" "$1"
}
warning() {
    echo -e "\033[1;33m[¡] $1 \033[0m" "$1"
}
success() {
    printf "\033[0;32m%s\033[0m\n" "$1"
}
info() {
    printf "\033[0;34m%s\033[0m\n" "$1"
}
debug() {
    printf "\033[1;30m%s\033[0m\n" "$1"
}

# Other functions
print() {
  
  error "error"
  warning "warning- haciendo pruebas"
  success "success"
  info "info"
  debug "debug"

}

# Params function
params() {

  for param in "$@"; do
    case "${param}" in
      -a|--alpha)
        alpha=true 
        ;;
      -b=*|--beta=*)
        beta=${param#*=}
        ;;
      -h|--help)
        usage
        exit 0
        ;;
      *)
        error "Unknown parameter ${param}"
        exit 1
        ;;
    esac
  done
}

# Main function
main() {
  print

  debug 'esto es una prueba'
}

main 