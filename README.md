<img src="./assets/SKiP_LOGO.png" hieght="250" width="350" title="SKiP">

[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/ItsSiddharth/SKiP/edit/master/LICENSE)[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com) 

:arrows_counterclockwise: SKiP is a tools designed to increase efficiency during your study hours.
 
 ## Usage
 1.Clone the repository

```
$ git clone https://github.com/ItsSiddharth/SKiP.git
```
2.Use the requirements.txt file to install all the required dependencies.

```
$ pip3 install -r requirements.txt
```

 3.Download <a href="http://nlp.stanford.edu/data/wordvecs/glove.6B.zip">glove.6B.zip</a> file from Standfords Github repository from the hyperlink.
 

> Unzip it and save the .txt file in the same folder as other files in the cloned repo


4.Have the video downloaded and saved a `vh.mp4`.

>If you want to follow the exact implementation that I have done download this <a href="https://www.youtube.com/watch?v=TlB_eWDSMt4&t=917s">Tutorial</a>

4.Now use the ` loading_model.py ` file to convert this model into a pickle file so that it loads fast

> Loading the model as a text file takes 9 minutes on my system but may vary in yours. The lead time will not go below 5 mins so pickling it is important as it brings down the load time in my system to 8 seconds.

5.Pass this code to an AWS bucket for it to transcribing i.

> The JSON AWS returns after transcribing will be critical in later stages. 

<img src="./assets/SKiP_AWS.png" width="350" title="AWS">

The <a href="https://www.youtube.com/watch?v=TlB_eWDSMt4&t=917s">Video</a> used to create the JSON in my repository is linked.

6.Rename the JSON to ` data.json `.

7.Run the ` main.py ` script with the topic you want to jump to as an argument.

> Here if I wanted to go to the part where Mosh taught Modules then I give a command as below

```
$ python main.py modules
```
> Say I wanted to go to the part where he teaches path module 

```
$ python main.py path
```

* **NOTE** : Please enter a single word as python argument.
* **NOTE** : As a prerequisite have VLC media player installed.

## LICENSE
<a href="https://github.com/ItsSiddharth/SKiP/blob/master/LICENSE">MIT</a>
