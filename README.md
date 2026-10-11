# Generador de Contraseñas

Aplicación de escritorio/móvil desarrollada en Python con [Flet](https://flet.dev/). La interfaz permite generar contraseñas y copiarlas al portapapeles.

## Estado actual

- Genera una contraseña al abrir la app y al cambiar sus opciones.
- Permite ajustar la longitud entre 8 y 32 caracteres (12 por defecto).
- Usa letras minúsculas y permite activar mayúsculas, números y símbolos.
- Permite generar otra contraseña y copiarla al portapapeles.
- Hay builds Android divididos por arquitectura en `src/build/apk/` (`arm64-v8a`, `armeabi-v7a` y `x86_64`). Los artefactos se generan localmente y no son necesarios para desarrollar.

La app sigue en desarrollo. El medidor de seguridad es actualmente fijo y no evalúa la contraseña. Además, el conjunto de caracteres puede conservar opciones que se activaron en generaciones anteriores. La generación usa el módulo estándar `random`, que no es criptográficamente seguro; no uses esta versión para crear contraseñas de cuentas sensibles.

## Requisitos

- Python 3.12
- Pipenv
- Para compilar Android: JDK 17 y Android SDK. Flet puede instalar las herramientas Android que falten durante la primera compilación; se necesita conexión a Internet.

## Preparar el entorno

Desde la raíz del repositorio, instala Pipenv si aún no está disponible y prepara el entorno con las versiones del lockfile:

```bash
python -m pip install --user pipenv
pipenv sync
```

El lockfile incluye Flet, pero no su CLI. Instala la CLI en el entorno del proyecto para poder ejecutar y compilar la app:

```bash
pipenv run pip install "flet[cli]==1.0.4"
```

## Ejecutar en modo desarrollo

Desde la raíz del repositorio:

```bash
pipenv run flet run src/main.py
```

Flet ejecuta la app en modo desarrollo y recarga los cambios al editar el código.

## Compilar para Android

Desde la raíz del repositorio, crea APK separados para las arquitecturas Android disponibles:

```bash
pipenv run flet build apk src --split-per-abi
```

Los APK se generan en `src/build/apk/`. Instala en un dispositivo conectado el archivo correspondiente a su arquitectura; por ejemplo, para la mayoría de los teléfonos Android actuales:

```bash
adb install src/build/apk/src-arm64-v8a.apk
```

Se requieren JDK 17 y Android SDK. La primera compilación puede descargar e instalar componentes adicionales. Consulta también la [guía oficial de compilación Android de Flet](https://flet.dev/docs/publish/android/).

## Estructura del código

- `src/app_model.py`: generación de contraseñas.
- `src/app_view.py`: interfaz y controles de la app.
- `src/app_controller.py`: conecta las acciones de la interfaz con el modelo.
- `src/main.py`: punto de entrada.

## Colaborar

1. Crea una rama para tu cambio a partir de la rama principal.
2. Instala el entorno siguiendo las instrucciones anteriores.
3. Ejecuta la app con `pipenv run flet run src/main.py` y prueba el flujo afectado. Actualmente no hay pruebas automatizadas para la lógica Python.
4. Abre un pull request con un resumen del cambio y los pasos de verificación; para cambios de interfaz, incluye una captura de pantalla.

Mantén los cambios de lógica, interfaz y eventos en sus módulos correspondientes. No añadas al control de versiones los artefactos generados en `build/`.

## Reconocimientos

- Icono de la app: https://www.pngegg.com/es/png-zkdmz
- Idea original: Código Espinoza - https://www.youtube.com/watch?v=TSLBwro2z0k