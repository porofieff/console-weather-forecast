#!/usr/bin/bash

echo "Вставьте ваш API ключ: "
read OW_API

echo "Вставьте вашу широту: "
read OW_LAT

echo "Вставьте вашу долготу: "
read OW_LON

echo "Ваш API ключ = $OW_API"
echo "Ваша широта = $OW_LAT"
echo "Ваша долгота = $OW_LON"

echo "Если все верно нажмите 1, иначе 2"
read choice

if [[ $choice == '1' ]]; then
  echo "export OW_API_KEY='$OW_API'" >> ~/.zshrc
  echo "export OW_LAT='$OW_LAT'" >> ~/.zshrc
  echo "export OW_LON='$OW_LON'" >> ~/.zshrc
  echo "Настройки сохранены! Не забудьте выполнить 'source ~/.zshrc'"
else
  echo "Перезапустите скрипт и внесите исправленные значения."
fi
