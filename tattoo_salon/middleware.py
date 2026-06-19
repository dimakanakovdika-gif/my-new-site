from django.utils.deprecation import MiddlewareMixin
from django.http import FileResponse
import os

class BrotliMiddleware(MiddlewareMixin):
    """Отдает Brotli-сжатые файлы с правильными заголовками"""
    
    def process_response(self, request, response):
        path = request.path
        
        # Если запрос к Unity файлам в Build/
        if '/game/Build/' in path and not path.endswith('.br'):
            # Проверяем, есть ли .br версия
            br_path = path + '.br'
            static_root = 'tattoo_salon/static'
            full_br_path = os.path.join(static_root, br_path.replace('/static/', ''))
            
            if os.path.exists(full_br_path):
                # Отдаем .br файл с правильными заголовками
                response = FileResponse(open(full_br_path, 'rb'))
                response['Content-Encoding'] = 'br'
                response['Vary'] = 'Accept-Encoding'
                
                # Content-Type по расширению оригинального файла
                if path.endswith('.js'):
                    response['Content-Type'] = 'application/javascript'
                elif path.endswith('.wasm'):
                    response['Content-Type'] = 'application/wasm'
                elif path.endswith('.data'):
                    response['Content-Type'] = 'application/octet-stream'
                    
        # Если уже .br файл - добавляем заголовок
        elif path.endswith('.br'):
            response['Content-Encoding'] = 'br'
            if path.endswith('.js.br'):
                response['Content-Type'] = 'application/javascript'
            elif path.endswith('.wasm.br'):
                response['Content-Type'] = 'application/wasm'
            elif path.endswith('.data.br'):
                response['Content-Type'] = 'application/octet-stream'
                
        return response