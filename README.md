# Console Weather Forecast
<div align="center">
  <a>
    <img src="media/weather_usage.gif" width="600" height="600">
  </a>
</div>

  

------------
## О проекте

Программа выводит в терминал основную информацию о текущей погоде. Для получения данных используется API сервиса OpenWeatherMap.


------------
## Установка

1) Вам нужно получить API ключ на сайте [OpenWeatherMap](https://openweathermap.org/current)
2) Узнать ваши GPS координаты.

3) Скопировать репозиторий
 ```sh
  git clone https://github.com/porofieff/console-weather-forecast.git
  ```

4) Создание симлинка на исполняемый файл, это позволит запускать приложение из любой точки в системе

```sh
  sudo ln -s $(pwd)/weather /usr/local/bin
  ```

5) Создать и активировать виртуальное окружение Python
```sh
  python3 -m venv .env
  source  .env/bin/activate
  ```

6) Скачать зависимости
```sh
  pip install -r requirements.txt
  ```

### Установка с помощью скрипта

Скрипт работает только с zsh, для корректной работы вам нужно либо изменить в `install.sh` _.zshrc_ на _.bashrc_, либо выполнить установку в ручную!

7) Дать права доступа для `install.sh`
```sh
  chmod +x install.sh
  ```

8) Запустить скрипт и ввести API ключ и GPS
```sh
  ./install.sh 
  ```

### Установка и настройка программы в ручную


7) Добавить в файл скрипта вашей оболочки API ключ и координаты. Данный пример для zsh, ваша оболочка может отличаться(bash, fish и др.)

```sh
  echo "export OW_API_KEY='{ваш ключ}'" >> ~/.zshrc
  echo "export OW_LAT='{ваша широта}'" >> ~/.zshrc
  echo "export OW_LON='{ваша долгота}'" >> ~/.zshrc
  source ~/.zshrc 
  ```
