#!/data/data/com.termux/files/usr/bin/env fish

if test (curl --socks5 localhost:9050 --socks5-hostname localhost:9050 -s https://check.torproject.org/api/ip)
    echo "YES"
else
    echo "NO"
    echo "Запускаю тор"
    tor -f torrc
    echo "Проверка связи"
    if test (curl --socks5 localhost:9050 --socks5-hostname localhost:9050 -s https://check.torproject.org/api/ip)
        echo "TOR запущен"
    else 
        echo "Не удалось запустить TOR"
    end
end

# curl --socks5 localhost:9050 --socks5-hostname localhost:9050 -s https://check.torproject.org/api/ip
