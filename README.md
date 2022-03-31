# desplazar_srt

with desplazar_srt.py you can correct your subtitles time ("\*.srt" Files).

- from your terminal you can do (without arguments):

> python3 desplazar_srt.py 

File path: .../Subtitle.srt
Seconds: 4

It will ask for the file path (example --> File path: /Users/myuser/Documents/mysubtitle.srt) 
and how many seconds you want to correct (Seconds can be positive or negative, example --> Seconds: 3 or Seconds: -2 )

At the end it will create a new file "desplazado.srt" in the same directory of the original sub file.

Also you can do it with arguments like this:

> python3 desplazar_srt.py "path" "seconds"

example: > python3 desplazar_srt.py "/Users/myuser/Documents/mysubtitle.srt" -2
