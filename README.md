# Tennis
This project has 2 main files, highlights.py and getForce.py. 

<h1> Highlights </h1>
highlights.py automatically generates highlights based on a video file in the parent folder (currently it is 'tennis.mp4'). It currently generates a 48 second highlight
on a 156 second clip (which itself is a highlight), which is a compression rate of about 70%. The highlight clip, original clip, and demonstration is found [here](https://drive.google.com/drive/folders/1Fgoms41m2Bh6Ef5XoEUyDaTIRQC6GI0V?usp=sharing).

<h1> Get Force </h1>
getForce.py identifies the force with which the ball moves after being served. It takes in a rally number as an input. The rally number is the index of a rally – in tennis.mp4 there are 5 rallies, so valid indices for rally number is 1-4. 
This function will not work if the starting part of the serve is cut (for example the footage for rally 2 does not include the starting part of the serve so this function doesn't work for rally 2). It may also not work if the server is on the far side of the court.
