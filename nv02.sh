#!/data/data/com.termux/files/usr/bin/env bash

curl 'https://nvspc.biz/api/dummy/getShowcase' \
  -H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux aarch64; rv:75.0) Gecko/20100101 Firefox/75.0' \
  -H 'Accept: */*' \
  -H 'Accept-Language: ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3' \
  --compressed \
  -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' \
  -H 'X-Requested-With: XMLHttpRequest' \
  -H 'Origin: https://nvspc.biz' \
  -H 'Connection: keep-alive' \
  -H 'Cookie: p=mPbapIVCWkIPz5Pw; S=ar7cN5HQykuyTdkNdUZwng; Dark=true' \
  -H 'TE: Trailers' \
  --data 'c=4H5U2pnf2kOy7-fO-5Pnbw&u=1&LNT=0&mic=0&mac=0&miw=0&maw=0&sortby=0&pad=6&count=10' |jq '.'
# curl 'https://nvspc.biz/api/dummy/getLotName' -H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux aarch64; rv:75.0) Gecko/20100101 Firefox/75.0' -H 'Accept: */*' -H 'Accept-Language: ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3' --compressed -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H 'X-Requested-With: XMLHttpRequest' -H 'Origin: https://nvspc.biz' -H 'Connection: keep-alive' -H 'Cookie: p=mPbapIVCWkIPz5Pw; S=ar7cN5HQykuyTdkNdUZwng; Dark=true' -H 'TE: Trailers' --data 'i=gwIob7OkY0uBN9zn80r4Nw'

1 'https://nvspc.biz/api/dummy/getLotName'
# curl 'https://nvspc.biz/api/dummy/getLotnameComments' -H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux aarch64; rv:75.0) Gecko/20100101 Firefox/75.0' -H 'Accept: */*' -H 'Accept-Language: ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3' --compressed -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H 'X-Requested-With: XMLHttpRequest' -H 'Origin: https://nvspc.biz' -H 'Connection: keep-alive' -H 'Cookie: p=mPbapIVCWkIPz5Pw; S=ar7cN5HQykuyTdkNdUZwng; Dark=true' -H 'TE: Trailers' --data 'i=gwIob7OkY0uBN9zn80r4Nw'
