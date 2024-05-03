# Harper
[![Coverage](https://harper.quantcore.space/v1/info/temapskov/harper/banner.svg)](https://harper.quantcore.space/v1/info/temapskov/harper/banner.svg)
___

`Harper` это помощник для разработчиков, который сможет помочь в решении различных
задач, связанных с разработкой программного обеспечения.

На текущий момент реализован функционал хранения и выдачи информации о процентном
покрытии репозитория тестами в виде `SVG`-баннера.

## Интерфейс

### REST API

#### `GET /v1/ping`

Эндпоинт для проверки работоспособности приложения.

Ответ:
```JSON
{
    "message": "pong"
}
```

#### `GET /v1/info/?repo_name=test&value=91`

Эндпоинт для сохраниния информации о процентном покрытии репозитория тестами.

Параметры:
- `repo_name` - название репозитория (строка)
- `value` - количество процентов (число)

Данный узел сохраняет информацию в базе данных приложения в формате ключ-значение.

#### `/v1/info/banner?repo_name=test`

Эндпоинт для получения баннера по имени репозитория, если такого не существует
вернется баннер со значением 0.

- `repo_name` - название репозитория (строка)

Ответ:
```svg
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="99" height="20">
  <linearGradient id="b" x2="0" y2="100%">
    <stop offset="0" stop-color="#bbb" stop-opacity=".1"/>
    <stop offset="1" stop-opacity=".1"/>
  </linearGradient>
  <mask id="a">
    <rect width="99" height="20" rx="3" fill="#fff"/>
  </mask>
  <g mask="url(#a)">
    <path fill="#555" d="M0 0h63v20H0z"/>
    <path fill="#9f9f9f" d="M63 0h36v20H63z"/>
    <path fill="url(#b)" d="M0 0h99v20H0z"/>
  </g>
  <g fill="#fff" text-anchor="middle" font-family="DejaVu Sans,Verdana,Geneva,sans-serif" font-size="11">
    <text x="31.5" y="15" fill="#9f9f9f" fill-opacity=".6">coverage</text>
    <text x="31.5" y="14">coverage</text>
    <text x="80" y="15" fill="#9f9f9f" fill-opacity=".6">0%</text>
    <text x="80" y="14">0%</text>
  </g>
</svg>
```

Вышеуказанный `SVG` код генерируется программой, в зависимости от процентного покрытия
может отличаться цветовая схема баннера.