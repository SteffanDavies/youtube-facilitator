# youtube-facilitator
Tools to help automate tasks for content creation

## Tools
----------
### Powershell
#### Create list of .mov files
Get-ChildItem -Path ./ -Name -filter *.mov | foreach {"file '$_'"} | out-file "list.txt" -encoding ASCII

### ffmpeg
#### Concatenate
ffmpeg -f concat -safe 0 -i list.txt -c copy output.mov

## Scripts
----------
### timestamps.py
From a collection of input movie files, create timestamps of them in alphabetical order, as if they were playing sequentially.
