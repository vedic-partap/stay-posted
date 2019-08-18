# stay-posted
Sends a free postcard a day from a monitored image folder. Run the script with any scheduler every 24h. If any images are inside the images folder, they will be sent to you as a postcard within few days. 

## Setup

You need the following folder structure in order to have a functioning script
<pre>
stay-posted  
|  
|---logs  
|    error.log  
|    stay-posted.log  
|  
|---images  
|    your.jpg  
|    images.jpg  
|    here.jpg  
|  
|---config  
|    user.json  
|    setup.json
</pre>
### Requirements
All requirements are listed in the requirements.txt file

## Credit
This script uses the [postcard-creator-wrapper](https://github.com/abertschi/postcard_creator_wrapper)
