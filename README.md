<h1> Red-black-tree</h1>
This is a dictionary which you can add and search its content using red black tree algorithm.

<p>
When you run the code it will display a menu which you can choose from to
<ol>
<li>Load</li>
<li>Print Dictionary Size</li>
<li>Insert word</li>
<li>Lookup a word</li>
<img src="assests/Screenshot (864).png"/>
</ol>
</p>
<p>
The dictionary name in the code is the same as the txt file uploaded in the repo, EN-US-Dictionary.

you can change it from the code
in this part:
<br/>
    def load(self, root):
    <br/>
        hand = open("EN-US-Dictionary.txt", "r")


</p>
<p>
To load the dictionary:
<br/>
Enter 1
<img src="assests/Screenshot (865).png"/>

To check the size of the tree
<br/>
Enter 2
<img src="assests/Screenshot (866).png"/>

To insert a word
<br/>
Enter 3
<br/>
if the word isn't in the dictionary, it will display "Word (the word you entered) inserted successfully" and will display both the tree size and height
<br/>

However if the word is present in the dictionary, it will display "Word already in the dictionary"
<img src="assests/Screenshot (867).png"/>

<br/>

To search for a word
<br/>
Enter 4
<br/>
if the word is present in the dictionary, it will display "Yes,word in the dictionary"
<img src="assests/Screenshot (868).png"/>
<br/>
However if the word isn't in the dictionary, it will display "No,word isn't in the dictionary"
<img src="assests/Screenshot (869).png>

</p>