Title: remembering the forest vs. the trees
Slug: tree
Date: 2018-07-22
Tags: memory, emotion, faces, cognitive neuroscience, data science
Image: /images/emo_icon.jpg

Think back to an old relationship you are now far-removed from. Early on in that relationship, you probably were wearing rose-colored glasses. Everything was great, he was the best, life was good. But, at that time, you were probably overlooking some red flags that turned out to really bug you later on. After a few months of bliss, it all fell apart. When you look back and reflect on that past relationship, you may only really remember the things you hated and why you moved on. Like how he would snore really loudly at night, or always forget to fill up the Brita with water. Just the major deal breakers.

In this example, the context shifted. When you were initially in the relationship, you were happy and in love and focused on the positive outlook of the relationship, As things soured, you started focusing on the details, and only saw traits that were a major turn off.

###background
It turns out there is a relationship between emotion and the types of information people pay attention to and remember. Positive emotions cause people to focus on the big picture, or, ‘see the forest instead of the trees’. Whereas negative emotion causes people to focus on the trees, without really noticing the forest.

A previous study demonstrated this relationship directly [(Gasper & Clore)](https://www.ncbi.nlm.nih.gov/pubmed/?term=gasper+clore+2002). In this study, the authors used modified Navon figures, which are big shapes made up of little shapes [(Kimchi & Palmer)](https://www.ncbi.nlm.nih.gov/pubmed/6214605). Subjects saw a shape on top of the screen (a big triangle made of small squares) that served as a cue. On the bottom of the screen, they saw two related shapes and were prompted to choose the image that was most similar to the cue.

![fig1](/images/shapes_mood.jpg)

Before subjects completed the task, they were instructed to write about either a positive experience or a negative experience from their past. Thinking and writing about a positive or negative event was enough to alter the mood of the participants. Interestingly, subjects who wrote about a positive experience were more likely to choose the object that was similar on the global level (the big triangle made of little squares), whereas subjects who wrote about a negative experience were more likely to focus on the local features (they chose the object made of little triangles). This study suggested that mood influences what type of information we pay attention to and deem most important for making decisions.



###emotion influences memory
These findings made me wonder how our current emotional state influences not only what we pay attention to, but also what we later remember about an experience.

I had to change a few key aspects of the prior attention study to investigate this phenomenon in a memory setting. First of all, I had to change the actual stimuli, because generic shapes made of other little shapes are not particularly memorable -- nor are they very realistic. But, local vs. global details are prevalent in plenty of naturally-occurring stimuli. For instance, houses have both local features like the windows, door, building material, and these elements fit together to form the the overall shape and style of the house.

I ended up opting for stimuli that we are all extremely familiar with: faces. Faces have both global and local information. The global information is the configuration of all of the facial features. The eyes are above the nose, which is above the mouth. We process this global information fluidly and expertly, as we are highly skilled at viewing faces (I don’t know about you, but I’ve been honing this expertise since I was a baby!). We also can process the local information about faces. I’m sure you can remember someone’s striking blue eyes or big crooked nose very vividly. But, we do rely more heavily on global information to process faces.

Here's a demonstration of how important global information is to recognize faces. We can disrupt the global processing, simply by flipping the face upside down. Take a look at the right-side up and upside-down faces [(Maurer, Le Grand, Mondloch)](https://www.ncbi.nlm.nih.gov/pubmed/12039607). They are pictures of the same face, right? Click the button to see the upside-down face flipped.

<input id="show_image" type="button" value="show/hide face"</>

<div class="clearfix">
<div class="column left_pic_3">
<img class="icon" src='/images/face1.png'>
</div>
<div class="column mid_pic_3">
<img src='/images/face2.png'>
</div>
<div class="column right_pic_3">
<!-- <input type="button" value="show face" onclick="showImage();"/>
<img id="loadingImage" src="/images/face3.png" style="visibility:hidden"/> -->

<!-- <a id="show_image">click here to show face</a> -->
<img id="face3" style="display:none;" src="images/face3.png">

</div>
</div>

Well, they are the same face, but the features have been re-arranged! You probably didn't even notice. This effect is called the "Thatcher effect", because the first experiment that manipulated faces in this way used an image of Margaret Thatcher [(Thompson, Peter)](https://www.ncbi.nlm.nih.gov/pubmed/?term=Margaret+Thatcher%3A+A+New+Illusion).

The second experimental feature I changed was the mood induction. Rather than having subjects write about an irrelevant past experience that was positive or negative, I tailored stories to be directly relevant to the faces participants studied for the memory test. In this way I harnessed the power of association to create positive vs. negative emotions related to specific faces. I wrote a bunch of happy and sad vignettes and had participants read one before studying a face. In this way, a happy or sad story was uniquely associated to each face.

![fig3](/images/face_task.png)

Later, I tested participants’ memory for the faces, by showing them the faces they’d seen before mixed with an equal number of brand new faces. Participants always studied the faces right-side up. However, at the test, they saw the face presented either right-side up or upside-down, and the associated story was not re-presented. Interestingly, I found that faces that had previously been associated with a happy story were remembered better than faces associated with a sad story when I tested memory for the faces in the upright position. On the other hand, memory for the upside down faces benefited when the faces had been associated with a sad story rather than a happy story. These results suggest that happy associations cause participants to pay attention to and remember global information whereas sad associations cause participants to pay attention to and remember local information. [(Bridge, 2010)](/pdfs/bridge10.pdf)

<div class="clearfix">
<div class="column left_pic">
<img class="icon" src='/images/emo_line_recall.png'>
</div>
<div class="column right_pic">
<img src='/images/emo_line_precision.png'>
</div>
</div>

<p align="center">
<img src="/images/emo_bar_f1.png" alt="f1" style="width:60%;"/>
</p>
<!-- ![fig4c](/images/emo_bar_f1.png) -->
###where does this study fall on the consciousness continuum?
In this task, subjects had to overtly make a behavioral response about whether they saw a face before or not. The main measure of memory I used was conscious. However, I would argue that the influence of emotion on how subjects processed the faces was unconscious. Subjects were not aware that they attended to more “local” features of Sad faces and more “global” features of happy faces. However, they likely viewed the faces differently when they studied them (unfortunately I did not have access to an eye tracker at the time of this experiment), which caused them to remember them differently on the final test.

###extrapolation & speculation
* Even though content you are presenting may not have any inherent positive or negative valence, the person you present it to might still have positive or negative associations with a topic that you consider neutral (e.g. memory of college for one person could be filled with happy nostalgia, whereas memory of college for another person could be encompassed by debilitating student debt).
* When presenting emotional material, you might have to adjust content so that the right level of details vs. overarching ideas get across the way you want them to.

###data & analysis
[emotion](https://github.com/donnajobridge/data_visualizations/tree/master/emo)
