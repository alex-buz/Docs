# Compile Jade template language into HTML
```
$ watchmedo shell-command \
      --patterns="*.jade" \
      --command='pyjade -c jinja "${watch_src_path}"' \  1
      --ignore-directories
```
# Convert an asciidoc to HTML
```
$ watchmedo shell-command \
      --patterns="*.asciidoc" \
      --command='asciidoctor "${watch_src_path}"' \  1
      --ignore-directories
```      
# Synchronize files to a server
```
$ watchmedo shell-command \
      --patterns="*" \
      --command='rsync -avz mydir/ host:/home/ubuntu"'
      
```

# Mail a file every time it changes!
```
$ watchmedo shell-command \
      --patterns="*" \
      --command='cat "${watch_src_path}" | ↲
      mail -s "New version" me@domain.com' \
      --ignore-directories      
```      


```python
from watchdog.observers import Observer
from watchdog.events import (
    PatternMatchingEventHandler, FileModifiedEvent,
    FileCreatedEvent)

observer = Observer()  1

class Handler(PatternMatchingEventHandler):
    def on_created(self, event: FileCreatedEvent):  2
        print('File Created: ', event.src_path)

    def on_modified(self, event: FileModifiedEvent):  2
        print('File Modified: %s [%s]' % (
        	event.src_path, event.event_type))

observer.schedule(event_handler=Handler('*'), path='.')  3
observer.daemon = False
observer.start()

try:
    observer.join() 4
except KeyboardInterrupt:
    print('Stopped.')
    observer.stop()
    observer.join()
```    
