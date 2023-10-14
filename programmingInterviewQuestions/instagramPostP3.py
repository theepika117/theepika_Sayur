'''
#3. No need to write a program. Just pseudocode is enough.Define a class for a instagram post. Define the properties and functions.
#Define which one will be private and which one public.


class instaPost :
    def selectContent() :
        #check for galary access
        if !access :
            #ask for access granting
        
        else :
            # show phots and videos in the galary
            #ask for single selection or multiple selection
            #ask whether they wanna take picture or post from gallery
            if takePicture :
                #check for galary access
                if !access :
                    #ask for access granting
        
                else : 
                    #show various filters available
                    # use filter as per users choice 
                    # take picture  or record video (private data member)
                    #taken picture is the item selected

            else :
                choice = 0 #choices they make is a private data member
                if singleSelection :
                    maxChoiceLimit = 1
                
                else :
                    maxChoiceLimit = 8
            
                while(choice <= maxChoiceLimit) :
                    #select item
                    itemSelected.append(selectedItem) #it is also a private data member
        return choice,itemSelected
    

    def editItems(choice,itemSelected[]) :
        #adjust grid position if needed
        #apply filters or edit items if needed as per user's choice
        #edit include adjusting brigthness,contrast,croping ,rotating
        #add music if needed as per user's choice
        #all changes made are private to the class
        
        return changesMade
    
    def sharePost(changesMade) :
        #ask for caption
        #add location as per user's choice
        #tag other people as per user's choice
        #share the post
        #shared post is a protected data member


#main code
#ask user whether they want to post
post1 = instaPost()

'''