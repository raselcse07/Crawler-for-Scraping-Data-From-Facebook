# This is a Simple Crawler to grab data from facebook using Facebook Graph API
# Name : Rasel Miah
# Email : rasel_cse07@yahoo.com

import facebook




def FacebookData(token):

    graph = facebook.GraphAPI(access_token=token, version='2.7')
    url="me?fields=id,name,about,birthday,email,education,work,devices,gender,hometown,feed.limit(10000){reactions,message,comments{from,created_time,message,comments}}"
    all_data = graph.get_object(id=url)

    file_name=all_data["name"]+"_"+all_data["id"]+".txt"

    # ID and Name

    print("Collecting Personal Informations .......\n")

    id=all_data["id"]
    name=all_data["name"]

    print("Writing ID and Name  .... \n")

    with open(file_name,"a") as fp:

        fp.write(" ***************** Personal Informations **********\n")
        fp.write("\n\nID : {}\n".format(id))
        fp.write("Name : {}\n".format(name))

    print("Successfully Wrote ID and Name.\n")

    # About

    print("Collecting About Informations ......\n")

    try:

        print("Writing About Data ....\n")
        about=all_data["about"]

        with open(file_name,"a") as fp:
            fp.write("About : \n".format(about))
        print("Successfully wrote about data.\n")

    except KeyError:
        print("****** ERROR : About Data Not Found!! ******\n")

    # Gender

    print("Collecting Gender Informations ...... \n")

    try:

        print("Writing Gender Informations ....\n")
        gender=all_data["gender"]

        with open(file_name,"a") as fp:
            fp.write("Gender : {}\n".format(gender))

        print("Successfully wrote gender Informations.\n")

    except KeyError:

        print("****** ERROR : Gender Informations Not Found !!! ********\n")

    # Email

    print("Collecting Email Informations ........ \n")

    try:

        print("Writing Email Informations ......\n")
        email=all_data["email"]

        with open(file_name,"a") as fp:
            fp.write("Email : {}\n".format(email))

        print("Successfully wrote email Informations.\n")

    except KeyError:

        print("****** ERROR : Email Informations Not Found !!! ********\n")

    # Hometown

    print("Collecting Hometown Informations ........\n")

    try :

        print("Writing Hometown Informations ......\n")
        hometown=all_data["hometown"]["name"]

        with open(file_name,"a") as fp:

            fp.write("Hometown : {}\n".format(hometown))

        print("Successfully wrote hometown Informations.\n")

    except KeyError:

        print("****** ERROR : Hometown Informations Not Found !!! ********\n")

    # Birthday

    print("Collecting Birthday Informations .........\n")

    try:

        print("Writing Birthday Informations .......\n")
        birthday=all_data["birthday"]

        with open(file_name,"a") as fp:

            fp.write("Birthday : {}\n".format(birthday))

        print("Successfully wrote birthday Informations.\n")

    except KeyError:

        print("****** ERROR : Birthday Informations Not Found !!! ********\n")

    # Device

    print("Collecting Device Informations .......\n")

    try:

        print("Writing Device Informations .......\n")
        d=all_data["devices"]

        for i in range(len(d)):
            device_list=d[i]
            os=device_list["os"]

            with open(file_name,"a") as fp:

                fp.write("OS : {}\n".format(os))

        print("Successfully wrote device Informations.\n")

    except KeyError:

        print("****** ERROR : Device Informations Not Found !!! ********\n")

    # Education

    print("Collecting Educational Informations .........\n")

    try:

        print("Writing Educational Informations ........\n")
        all_education_data=all_data["education"]

        with open(file_name,"a") as fp:
            fp.write("\n**************** Educationl Informations *************\n\n")

        for i in range(len(all_education_data)):

            edu_dict=all_education_data[i]

            id=edu_dict["id"]
            type=edu_dict["type"]
            school=edu_dict["school"]
            year=edu_dict["year"]


            with open(file_name,"a") as fp:
                fp.write("ID : {}\n".format(id))
                fp.write("Type : {}\n".format(type))
                fp.write("Institute : {}\n".format(school["name"]))
                fp.write("Passing Year : {}\n".format(year["name"]))

            try:
                concentration_list=edu_dict["concentration"]
                for i in range(len(concentration_list)):
                    concentration_dict=concentration_list[i]

                    with open(file_name,"a") as fp:

                        fp.write("Degree Name : {}\n".format(concentration_dict["name"]))

            except KeyError:
                pass

            with open(file_name,"a") as fp:
                fp.write("\n")

        print("Successfully wrote educational Informations\n")

    except KeyError:

        print("****** ERROR : Educationl Informations Not Found !!! ********\n")


    # Work History

    print("Collecting Work History Informations ............\n")

    try:

        print("Writing Work History Informations .........\n")
        work_data=all_data["work"]

        with open(file_name,"a") as fp:

            fp.write("\n**************** Work History *************\n\n")

        for i in range(len(work_data)):

            work_dict=work_data[i]

            company_name=work_dict["employer"]["name"]
            company_location=work_dict["location"]["name"]
            company_position=work_dict["position"]["name"]
            start_date=work_dict["start_date"]


            with open(file_name,"a") as fp:

                fp.write("Compnay Name : {}\n".format(company_name))
                fp.write("Location : {}\n".format(company_location))
                fp.write("Postion : {}\n".format(company_position))
                fp.write("Start Date : {}\n".format(start_date))

            try:
                end_date=work_dict["end_date"]

                with open(file_name,"a") as fp:

                    fp.write("End Date : {}\n".format(end_date))

            except KeyError:
                pass


            with open(file_name,"a") as fp:

                fp.write("\n")

        print("Successfully wrote work history Informations.\n")

    except KeyError:

        print("****** ERROR : Work History Informations Not Found !!! ********\n")


    # Posts and comments

    print("Collecting Posts and Comments .................\n")

    try:

        print("Writing Posts and Comments ...........\n")

        posts=all_data["feed"]["data"]

        with open(file_name,"a") as fp:

            fp.write("\n**************** Posts and Comments *************\n\n")

        for i in range(len(posts)):

            posts_=posts[i]

            # Posts ID

            with open(file_name,"a") as fp:

                fp.write("**** Post-{} ****\n\n".format(i+1))
                fp.write("Posts ID : %s \n" % (posts_["id"]))

            # Status

            try:

                with open(file_name,"a") as fp:

                    fp.write("Posts : %s\n\n" %(posts_["message"]))

            except KeyError:
                pass

            # Reactions

            try:

                with open(file_name,"a") as fp:

                    fp.write("\n******* Reactions on this posts *******\n\n")

                reactions=posts_["reactions"]["data"]

                for i in range(len(reactions)):

                    reactions_dict=reactions[i]

                    with open(file_name,"a") as fp:
                        fp.write("Name : {}\n".format(reactions_dict["name"]))
                        fp.write("Type : {}\n".format(reactions_dict["type"]))
                        fp.write("\n")

            except KeyError:
                pass

            # Comments
            try:
                comments=posts_["comments"]["data"]

                with open(file_name,"a") as fp:

                    fp.write("\n**** Comments on this posts *****\n\n")

                for i in range(len(comments)):

                    comments_data=comments[i]

                    with open(file_name,"a") as fp:

                        fp.write("*** Comments-{} ***\n\n".format(i+1))
                        fp.write("Comments ID : %s\n" %(comments_data["id"]))
                        fp.write("Created Time : %s\n" %(comments_data["created_time"]))

                    # Comments Creator

                    comments_from=comments_data["from"]

                    with open(file_name,"a") as fp:

                        fp.write("Name : %s \n" % (comments_from["name"]))
                        fp.write("Comments Contents : %s\n" %(comments_data["message"]))

                    # Comments reply

                    try:

                        reply_data=comments_data["comments"]["data"]

                        with open(file_name,"a") as fp:

                            fp.write("\n***** reply ****\n\n")

                        for i in range(len(reply_data)):

                            reply_dict=reply_data[i]
                            created_time=reply_dict["created_time"]
                            from_reply=reply_dict["from"]["name"]
                            reply_mgs=reply_dict["message"]

                            with open(file_name,"a") as fp:

                                fp.write("Created Time : {}\n".format(created_time))
                                fp.write("Name : {}\n".format(from_reply))
                                fp.write("Reply : {}\n".format(reply_mgs))


                    except KeyError:
                        pass

                    with open(file_name,"a") as fp:

                        fp.write("\n")

            except KeyError:

                pass


            with open(file_name,"a") as fp:

                fp.write("\n")

        print("Successfully wrote Posts and Comments.\n")

    except KeyError:

        print("****** ERROR : Work History Informations Not Found !!! ********\n")

    print("Done !!!")

if __name__ == '__main__':

    file_name="token.txt"

    with open(file_name,"r") as token_list:

        token = token_list.read().splitlines()

        for i in range(len(token)):

            print("Using Token-{}".format(i+1))
            FacebookData(token[i])
