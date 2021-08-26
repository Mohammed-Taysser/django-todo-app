
## new project `urls`

```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('todo.urls', 'home'), namespace='home')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

## submit on `select` change

```html
onchange='submit()'
```
# django-todo-app
