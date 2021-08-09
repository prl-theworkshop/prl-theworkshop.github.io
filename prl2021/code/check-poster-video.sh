#!/bin/bash
PREFIX="../papers/PRL2021_paper_ ../videos/PRL2021_video_ ../posters/PRL2021_poster_ ../slides/PRL2021_slides_"
usage() {
  echo Usage: $0 '(-c | -o)' '<easychair id>'
  echo '-c': check if file exists
  echo '-o': open existing files
  echo
  echo searches for $PREFIX
  exit 1
}
if [[ $# -le 1 || $# -ge 3 ]] ; then
  usage
fi

check_file() {
  n=$1
  d=$2
  ls ${x}${n}.*
}

open_file() {
  n=$1
  d=$2
  open ${x}${n}.*
}

iterate() {
  for x in $PREFIX; do
    $1 $2 $x
  done

}

case $1 in
  '-c')
    iterate check_file $2
    ;;

  '-o')
    iterate open_file $2
    ;;

  *)
    usage
    ;;
esac
