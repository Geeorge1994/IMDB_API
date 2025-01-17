
from unittest.mock import  patch
import http.client
from ConnectionApi import APIMovie
import unittest
import Movie

class TestApiConect(unittest.TestCase):
    #TEST UNITARIOS
    
    @patch("ConnectionApi.APIMovie.searchMovieTitle") 
    def test_searchMovieTitle(self, mockss): 

        cases = (("Alien Abduction",          200,  ["tt2510434", "Alien Abduction", 2014],           "{'movie_results': [{'title': 'Alien Abduction', 'year': 2014, 'imdb_id': 'tt2510434'}],  'search_results': 4, 'status': 'OK', 'status_message': 'Query was successful'}"),
                 ("Alien Domicile 2: Lot 24", 200,  ["tt6853580", "Alien Domicile 2: Lot 24", 2019],  "{'movie_results': [{'title': 'Alien Domicile 2: Lot 24', 'year': 2019, 'imdb_id': 'tt6853580'}], 'search_results': 1, 'status': 'OK', 'status_message': 'Query was successful'}"),
                 ("Tesis",                    200,  "Sin resultados",                                 "{'search_results': 0, 'status': 'OK', 'status_message': 'Query was successful'}"),
                 ("&$%&/(",                   403,  "ERROR IN API CONNECTION",                        "ERROR IN API CONNECTION")  )

        for inptt, estatus, val_esp, mock_json in cases:   
            mockss.return_value.status_code = estatus
            mockss.return_value.json = mock_json
            fin_outpt = APIMovie().searchMovieTitle(inptt)
            self.assertEqual(fin_outpt, val_esp)
    

    
    @patch("http.client.HTTPResponse")
    def test_searchMovieDetails(self, mockss):
        
         cases = (("tt2510434", 200, ['A vacationing family encounters an alien threat in this pulse-pounding thriller based on the real-life Brown Mountain Lights phenomenon in North Carolina.', 'Janine Gosselin, Matty Beckerman', 'Katherine Sigimund, Corey Eid, Riley Polanski, Jillian Clare, Jeff Bowser, Peter Holden, Walter Phelan, Jordan Turchin, Kelley Hinman, Ben Sharples, Katherine Sigismund, Matty Beckerman, Ronald B. Bishop, Daniel Caton, Rick Chambers, Ray Chavez Jr., Mike Holley, Caleb Moody, Michael Turchin, Joshua P. Warren', 'Horror, Sci-Fi, Thriller, Action, Science Fiction'], "{'title': 'Alien Abduction', 'description': 'A vacationing family encounters an alien threat in this pulse-pounding thriller based on the real-life Brown Mountain Lights phenomenon in North Carolina.', 'year': '2014', 'release_date': '2014-04-04', 'imdb_id': 'tt2510434', 'imdb_rating': '5.1', 'vote_count': '188', 'popularity': '18.144', 'youtube_trailer_key': '6fDAap9JDwA', 'rated': 'NR', 'runtime': 85, 'genres': ['Horror', 'Sci-Fi', 'Thriller', 'Action', 'Science Fiction'], 'stars': ['Katherine Sigimund', 'Corey Eid', 'Riley Polanski', 'Jillian Clare', 'Jeff Bowser', 'Peter Holden', 'Walter Phelan', 'Jordan Turchin', 'Kelley Hinman', 'Ben Sharples', 'Katherine Sigismund', 'Matty Beckerman', 'Ronald B. Bishop', 'Daniel Caton', 'Rick Chambers', 'Ray Chavez Jr.', 'Mike Holley', 'Caleb Moody', 'Michael Turchin', 'Joshua P. Warren'], 'directors': ['Janine Gosselin', 'Matty Beckerman'], 'countries': ['United States of America'], 'language': ['English', 'Deutsch', 'Español', 'en'], 'status': 'OK', 'status_message': 'Query was successful'}"),
                  ("tt6853580", 200, ['When Rachel is extended an invitation to stay at the camping lot (Lot 24) of her missing uncle, she is leery, but excited at the thought of spending some time away. Although the details surrounding his disappearance are sketchy at best, Rachel and her friends plan a weekend of hiking and relaxing.', 'Curtis Johnson', 'Shane Franklin, Trenell Blanks, Aby Smidt, Nijah Fudge, Jordan Johnson, Decklan McGee, Kathryn Whitney, Enoch Greenhood', 'Horror, Sci-Fi, Action, Thriller, Science Fiction'], "{'title': 'Alien Domicile 2: Lot 24', 'description': 'When Rachel is extended an invitation to stay at the camping lot (Lot 24) of her missing uncle, she is leery, but excited at the thought of spending some time away. Although the details surrounding his disappearance are sketchy at best, Rachel and her friends plan a weekend of hiking and relaxing.', 'year': '2019', 'release_date': '2019-12-13', 'imdb_id': 'tt6853580', 'imdb_rating': '1.5', 'vote_count': '2', 'popularity': '2.578', 'youtube_trailer_key': 'byPTdCHAiyU', 'rated': None, 'runtime': 75, 'genres': ['Horror', 'Sci-Fi', 'Thriller', 'Science Fiction'], 'stars': ['Shane Franklin', 'Trenell Blanks', 'Aby Smidt', 'Nijah Fudge', 'Jordan Johnson', 'Decklan McGee', 'Kathryn Whitney', 'Enoch Greenhood'], 'directors': ['Curtis Johnson'], 'countries': ['USA'], 'language': ['English', 'en', 'Deutsch'], 'status': 'OK', 'status_message': 'Query was successful'}"),
                  ("tt7784604", 200, ["When Ellen, the matriarch of the Graham family, passes away, her daughter's family begins to unravel cryptic and increasingly terrifying secrets about their ancestry.", 'Ari Aster, Lex Hogan, Briana Wall, Mao Zedong', 'Toni Collette, Alex Wolff, Gabriel Byrne, Milly Shapiro, Ann Dowd, Christy Summerhays, Mallory Bechtel, Brock McKinney, Jake Brown, Morgan Lund, Jarrod Phillips, Heidi Méndez, Zachary Arthur, Moises L. Tovar, Austin R. Grant, Gabriel Monroe Eckert, Bus Riley, Harrison Neil, BriAnn Rachele, David Stanley, Ari Aster, Mark Blockovich, Kathleen Chalfant, John Forker, Rachelle Hardy, Marilyn Miller, Jason Miyagi, Lorenzo Silva, Alexis Long, Harrison Nell, Shane Morrisun, A.J. Moss, Georgia Puckett, Travis Sanchez', 'Horror, Mystery, Thriller, Action, Drama'], """{'title': 'Hereditary', 'description': "When Ellen, the matriarch of the Graham family, passes away, her daughter's family begins to unravel cryptic and increasingly terrifying secrets about their ancestry.", 'year': '2018', 'release_date': '2018-06-07', 'imdb_id': 'tt7784604', 'imdb_rating': '7.2', 'vote_count': '4528', 'popularity': '31.493', 'youtube_trailer_key': 'oU3tgpZbGIE', 'rated': 'R', 'runtime': 127, 'genres': ['Horror', 'Mystery', 'Thriller', 'Action', 'Drama'], 'stars': ['Toni Collette', 'Alex Wolff', 'Gabriel Byrne', 'Milly Shapiro', 'Ann Dowd', 'Christy Summerhays', 'Mallory Bechtel', 'Brock McKinney', 'Jake Brown', 'Morgan Lund', 'Jarrod Phillips', 'Heidi Méndez', 'Zachary Arthur', 'Moises L. Tovar', 'Austin R. Grant', 'Gabriel Monroe Eckert', 'Bus Riley', 'Harrison Neil', 'BriAnn Rachele', 'David Stanley', 'Ari Aster', 'Mark Blockovich', 'Kathleen Chalfant', 'John Forker', 'Rachelle Hardy', 'Marilyn Miller', 'Jason Miyagi', 'Lorenzo Silva', 'Alexis Long', 'Harrison Nell', 'Shane Morrisun', 'A.J. Moss', 'Georgia Puckett', 'Travis Sanchez'], 'directors': ['Ari Aster', 'Lex Hogan', 'Briana Wall', 'Mao Zedong'], 'countries': ['United States of America', 'USA'], 'language': ['English', 'en'], 'status': 'OK', 'status_message': 'Query was successful'}"""),
                  ("tt853580",  200, ['No hay directores para esta película', 'No hay actores para esta película', 'No hay generos para esta película'], "{'rated': None, 'runtime': None, 'genres': None, 'stars': None, 'directors': None, 'countries': None, 'language': None, 'status': 'OK', 'status_message': 'Query was successful'}"),
                  ("",          200, ['No hay directores para esta película', 'No hay actores para esta película', 'No hay generos para esta película'], "{'rated': None, 'runtime': None, 'genres': None, 'stars': None, 'directors': None, 'countries': None, 'language': None, 'status': 'OK', 'status_message': 'Query was successful'}"),
                  ("(&$%&/,",   403,  "ERROR IN API CONNECTION", "{'status': 'Error, wrong imdb ID format', 'status_message': 'Query Failed'}"))    


         for idd, estatus, val_esp, mock_json in cases:  
             mockss.return_value.status_code = estatus
             mockss.return_value.json = mock_json
             finn = APIMovie().searchMovieDetails(idd)
             self.assertEqual(finn, val_esp)
    
    @patch("http.client.HTTPResponse")
    def test_searchMovieImage(self, mockss):
         
 
         cases = (("tt2510434", 200, 'http://image.tmdb.org/t/p/original/pe9mSStpQC2doKtYY3VDJdBEBHr.jpg', "{'title': 'Alien Abduction', 'IMDB': 'tt2510434', 'poster': 'http://image.tmdb.org/t/p/original/pe9mSStpQC2doKtYY3VDJdBEBHr.jpg', 'fanart': 'http://image.tmdb.org/t/p/original/6BCGb7R4XF1mQsCaJsIel0QgIqo.jpg', 'status': 'OK', 'status_message': 'Query was successful'}"),
                  ("tt6853580", 200, 'http://image.tmdb.org/t/p/original/erwCgeDAlaCQCNShTl3S0COOj2A.jpg', "{'title': 'Alien Domicile 2: Lot 24', 'IMDB': 'tt6853580', 'poster': 'http://image.tmdb.org/t/p/original/erwCgeDAlaCQCNShTl3S0COOj2A.jpg', 'fanart': '', 'status': 'OK', 'status_message': 'Query was successful'}"),
                  ("tt7784604", 200, 'http://image.tmdb.org/t/p/original/4GFPuL14eXi66V96xBWY73Y9PfR.jpg', "{'title': 'Hereditary', 'IMDB': 'tt7784604', 'poster': 'http://image.tmdb.org/t/p/original/4GFPuL14eXi66V96xBWY73Y9PfR.jpg', 'fanart': 'http://image.tmdb.org/t/p/original/4DUoPZOHdPuROP4nyEIsPaMIiQl.jpg', 'status': 'OK', 'status_message': 'Query was successful'}"),
                  ("tt853580",  200, 'No hay poster para esta pelicula',                                   "{'status': 'not found', 'status_message': 'Query failed'}"),
                  ("",          200, 'No hay poster para esta pelicula',                                   "{'status': 'not found', 'status_message': 'Query failed'}"),
                  ("&$%&/(",    403, "ERROR IN API CONNECTION",                                            "{'rated': None, 'runtime': None, 'genres': None, 'stars': None, 'directors': None, 'countries': None, 'language': None, 'status': 'OK', 'status_message': 'Query was successful'}"))

         for idd,stts, val_esp, mock_json in cases:
             mockss.return_value.status_code = stts
             fin_outpt = APIMovie().searchMovieImage(idd) 
             mockss.return_value.json = mock_json        
             self.assertEqual("".join(fin_outpt)  , val_esp)
            

        
    @patch("http.client.HTTPResponse")
    def test_get_movie_titles(self, mockss):
         
         cases = (("Alien",        200, ['27 Alien Encounters', 'Abducted by Aliens: UFO Encounters of the 4th Kind', 'AC1: Alien Contamination', 'Alien 2: On Earth', 'Alien 51', 'Alien Abdicktion', 'Alien Abduction', 'Alien Abduction: Incident in Lake County', 'Alien Addiction', 'Alien Adventure', 'Alien Agenda', 'Alien Agent', 'Alien Apocalypse', 'Alien Armageddon', 'Alien Arsenal', 'Alien Artifacts: The Lost World', 'Alien Autopsy', 'Alien Autopsy: (Fact or Fiction?)', 'Alien Avengers II', 'Alien Babes', 'Alien Beach Party Massacre', 'Alien Beasts', 'Alien Blood', 'Alien Cargo', 'Alien Chronicles Top Ufo Encounters', 'Alien Code', 'Alien Contact: NASA Exposed 2', 'Alien Contact: Outer Space', 'Alien Contact: Secret Societies', 'Alien Contactee: A Conversation with Dr.Louis Turi', 'Alien Convergence', 'Alien Crash at Roswell: The UFO Truth Lost in Time', 'Alien Creatures from Beyond: Monsters, Ghosts and Vampires', 'Alien Crystal Palace', 'Alien Dawn', 'Alien Domicile 2: Lot 24', 'Alien Domicile', 'Alien Dreamtime', 'Alien Earths', 'Alien Encounters from New Tomorrowland', 'Alien Escape', 'Alien Evolution', 'Alien Expedition', 'Alien Express', 'Alien Factor 2: The Alien Rampage', 'Alien from Area 51: The Alien Autopsy Footage Revealed', 'Alien from L.A.', 'Alien from the Darkness'], "{'movie_results': [{'title': '27 Alien Encounters', 'year': 2016, 'imdb_id': 'tt5993146'}, {'title': 'Abducted by Aliens: UFO Encounters of the 4th Kind', 'year': 2014, 'imdb_id': 'tt4205864'}, {'title': 'AC1: Alien Contamination', 'year': 2014, 'imdb_id': 'tt4068016'}, {'title': 'Alien 2: On Earth', 'year': 1980, 'imdb_id': 'tt0078749'}, {'title': 'Alien 51', 'year': 2004, 'imdb_id': 'tt0384803'}, {'title': 'Alien Abdicktion', 'year': 2009, 'imdb_id': 'tt1545003'}, {'title': 'Alien Abduction', 'year': 2014, 'imdb_id': 'tt2510434'}, {'title': 'Alien Abduction', 'year': 2005, 'imdb_id': 'tt0426396'}, {'title': 'Alien Abduction: Incident in Lake County', 'year': 1998, 'imdb_id': 'tt0142074'}, {'title': 'Alien Addiction', 'year': 2018, 'imdb_id': 'tt5028702'}, {'title': 'Alien Adventure', 'year': 1999, 'imdb_id': 'tt0238829'}, {'title': 'Alien Agenda', 'year': 2010, 'imdb_id': 'tt2043773'}, {'title': 'Alien Agenda', 'year': 2019, 'imdb_id': 'tt9032972'}, {'title': 'Alien Agent', 'year': 2007, 'imdb_id': 'tt0820466'}, {'title': 'Alien Apocalypse', 'year': 2005, 'imdb_id': 'tt0404756'}, {'title': 'Alien Armageddon', 'year': 2011, 'imdb_id': 'tt1910498'}, {'title': 'Alien Arsenal', 'year': 1999, 'imdb_id': 'tt0200421'}, {'title': 'Alien Artifacts: The Lost World', 'year': 2019, 'imdb_id': 'tt10463274'}, {'title': 'Alien Autopsy', 'year': 2006, 'imdb_id': 'tt0466664'}, {'title': 'Alien Autopsy: (Fact or Fiction?)', 'year': 1995, 'imdb_id': 'tt0163521'}, {'title': 'Alien Avengers II', 'year': 1997, 'imdb_id': 'tt0118581'}, {'title': 'Alien Babes', 'year': 2009, 'imdb_id': 'tt4022932'}, {'title': 'Alien Beach Party Massacre', 'year': 1996, 'imdb_id': 'tt0313187'}, {'title': 'Alien Beasts', 'year': 1991, 'imdb_id': 'tt0122882'}, {'title': 'Alien Blood', 'year': 1999, 'imdb_id': 'tt0191774'}, {'title': 'Alien Cargo', 'year': 1999, 'imdb_id': 'tt0184197'}, {'title': 'Alien Chronicles Top Ufo Encounters', 'year': 2020, 'imdb_id': 'tt13097240'}, {'title': 'Alien Code', 'year': 2017, 'imdb_id': 'tt5453522'}, {'title': 'Alien Contact: NASA Exposed 2', 'year': 2017, 'imdb_id': 'tt7131060'}, {'title': 'Alien Contact: Outer Space', 'year': 2017, 'imdb_id': 'tt7130832'}, {'title': 'Alien Contact: Secret Societies', 'year': 2015, 'imdb_id': 'tt5818768'}, {'title': 'Alien Contactee: A Conversation with Dr.Louis Turi', 'year': 2020, 'imdb_id': 'tt12338276'}, {'title': 'Alien Convergence', 'year': 2017, 'imdb_id': 'tt6874406'}, {'title': 'Alien Crash at Roswell: The UFO Truth Lost in Time', 'year': 2013, 'imdb_id': 'tt2778282'}, {'title': 'Alien Creatures from Beyond: Monsters, Ghosts and Vampires', 'year': 2015, 'imdb_id': 'tt7130684'}, {'title': 'Alien Crystal Palace', 'year': 2018, 'imdb_id': 'tt7254808'}, {'title': 'Alien Dawn', 'year': 2012, 'imdb_id': 'tt2275499'}, {'title': 'Alien Domicile 2: Lot 24', 'year': 2019, 'imdb_id': 'tt6853580'}, {'title': 'Alien Domicile', 'year': 2017, 'imdb_id': 'tt6574700'}, {'title': 'Alien Dreamtime', 'year': 2003, 'imdb_id': 'tt0371519'}, {'title': 'Alien Earths', 'year': 2009, 'imdb_id': 'tt1517549'}, {'title': 'Alien Encounters from New Tomorrowland', 'year': 1995, 'imdb_id': 'tt0235174'}, {'title': 'Alien Escape', 'year': 1996, 'imdb_id': 'tt0112318'}, {'title': 'Alien Evolution', 'year': 2001, 'imdb_id': 'tt0297720'}, {'title': 'Alien Expedition', 'year': 2018, 'imdb_id': 'tt8305690'}, {'title': 'Alien Express', 'year': 2005, 'imdb_id': 'tt0450258'}, {'title': 'Alien Factor 2: The Alien Rampage', 'year': 2001, 'imdb_id': 'tt0413669'}, {'title': 'Alien from Area 51: The Alien Autopsy Footage Revealed', 'year': 2012, 'imdb_id': 'tt2395137'}, {'title': 'Alien from L.A.', 'year': 1988, 'imdb_id': 'tt0092532'}, {'title': 'Alien from the Darkness', 'year': 1997, 'imdb_id': 'tt0421577'}], 'search_results': 50, 'status': 'OK', 'status_message': 'Query was successful'}"),
                  ("Help",         200, ["A Child's Cry for Help", 'A Cry for Help', 'A Cry for Help: The Tracey Thurman Story', 'A Little Help', "Can't Help Falling in Love", "Craig Ferguson: I'm Here to Help", 'Cry for Help', 'Dangshinui Hawooseuhelpeo', 'Davey and Goliath: Vol. 4: Helping Each Other', 'Dial: Help', 'God Help the Girl', 'Heaven Can Help', "Heaven Help Me, I'm In Love", 'Heaven Help Us', 'Help for the Holidays', 'Help Me I Am Dead', 'Help Me, Eros', "Help! I'm A Fish", 'Help!', 'Help', 'Help, Help, the Globolinks!', 'Help, I Shrunk My Friends', 'Help, I Shrunk My Parents', 'Help, I Shrunk My Teacher', "Help, What's Killing Me?", 'Helpless and Reckless', 'Helpless', 'Helpmates', "Katya: Help Me, I'm Dying", 'Lord Help Us', 'Metallica Helping Hands Concert & Auction: Live & Acoustic From HQ', "Mother's Little Helpers", "Santa's Little Helper", "Santa's Little Helpers", "Satan's Little Helper", 'Scream for Help', 'Self Helpless', 'So Help Me God', 'So Help Us God', 'Somebody Help Me 2', 'Somebody Help Me', 'Strawberry Shortcake: Berry Big Help', "Super Monsters: Santa's Super Monster Helpers", "The Girl Can't Help It", 'The Help', 'The Helpers'], """{'movie_results': [{'title': "A Child's Cry for Help", 'year': 1994, 'imdb_id': 'tt0109413'}, {'title': 'A Cry for Help', 'year': 1975, 'imdb_id': 'tt0072834'}, {'title': 'A Cry for Help: The Tracey Thurman Story', 'year': 1989, 'imdb_id': 'tt0097132'}, {'title': 'A Little Help', 'year': 2010, 'imdb_id': 'tt1319722'}, {'title': "Can't Help Falling in Love", 'year': 2017, 'imdb_id': 'tt6725484'}, {'title': "Craig Ferguson: I'm Here to Help", 'year': 2013, 'imdb_id': 'tt2523852'}, {'title': 'Cry for Help', 'year': 2005, 'imdb_id': 'tt0441747'}, {'title': 'Cry for Help', 'year': 2009, 'imdb_id': 'tt1437596'}, {'title': 'Dangshinui Hawooseuhelpeo', 'year': 2018, 'imdb_id': 'tt8487888'}, {'title': 'Davey and Goliath: Vol. 4: Helping Each Other', 'year': 1962, 'imdb_id': 'tt0055667'}, {'title': 'Dial: Help', 'year': 1988, 'imdb_id': 'tt0095952'}, {'title': 'God Help the Girl', 'year': 2014, 'imdb_id': 'tt2141751'}, {'title': 'Heaven Can Help', 'year': 1984, 'imdb_id': 'tt0088096'}, {'title': "Heaven Help Me, I'm In Love", 'year': 2005, 'imdb_id': 'tt0473212'}, {'title': 'Heaven Help Us', 'year': 1985, 'imdb_id': 'tt0089264'}, {'title': 'Help for the Holidays', 'year': 2013, 'imdb_id': 'tt2374486'}, {'title': 'Help Me I Am Dead', 'year': 2013, 'imdb_id': 'tt3430634'}, {'title': 'Help Me, Eros', 'year': 2007, 'imdb_id': 'tt1076251'}, {'title': "Help! I'm A Fish", 'year': 2000, 'imdb_id': 'tt0168856'}, {'title': 'Help!', 'year': 1965, 'imdb_id': 'tt0059260'}, {'title': 'Help', 'year': 2010, 'imdb_id': 'tt1663647'}, {'title': 'Help, Help, the Globolinks!', 'year': 1969, 'imdb_id': 'tt2240708'}, {'title': 'Help, I Shrunk My Friends', 'year': 2021, 'imdb_id': 'tt11541220'}, {'title': 'Help, I Shrunk My Parents', 'year': 2018, 'imdb_id': 'tt6818140'}, {'title': 'Help, I Shrunk My Teacher', 'year': 2015, 'imdb_id': 'tt4141024'}, {'title': "Help, What's Killing Me?", 'year': 2015, 'imdb_id': 'tt4558462'}, {'title': 'Helpless and Reckless', 'year': 2012, 'imdb_id': 'tt2330829'}, {'title': 'Helpless', 'year': 2012, 'imdb_id': 'tt2308725'}, {'title': 'Helpless', 'year': 1996, 'imdb_id': 'tt0116515'}, {'title': 'Helpmates', 'year': 1932, 'imdb_id': 'tt0022994'}, {'title': "Katya: Help Me, I'm Dying", 'year': 2019, 'imdb_id': 'tt11283990'}, {'title': 'Lord Help Us', 'year': 2006, 'imdb_id': 'tt3270130'}, {'title': 'Lord Help Us', 'year': 2007, 'imdb_id': 'tt0418223'}, {'title': 'Metallica Helping Hands Concert & Auction: Live & Acoustic From HQ', 'year': 2020, 'imdb_id': 'tt12453134'}, {'title': "Mother's Little Helpers", 'year': 2005, 'imdb_id': 'tt0439256'}, {'title': "Mother's Little Helpers", 'year': 2019, 'imdb_id': 'tt9100838'}, {'title': "Santa's Little Helper", 'year': 2015, 'imdb_id': 'tt4592572'}, {'title': "Santa's Little Helpers", 'year': 2019, 'imdb_id': 'tt9540768'}, {'title': "Satan's Little Helper", 'year': 2004, 'imdb_id': 'tt0380687'}, {'title': 'Scream for Help', 'year': 1984, 'imdb_id': 'tt0088066'}, {'title': 'Self Helpless', 'year': 2011, 'imdb_id': 'tt1434449'}, {'title': 'So Help Me God', 'year': 2018, 'imdb_id': 'tt5501158'}, {'title': 'So Help Us God', 'year': 2017, 'imdb_id': 'tt7165516'}, {'title': 'Somebody Help Me 2', 'year': 2010, 'imdb_id': 'tt1760998'}, {'title': 'Somebody Help Me', 'year': 2007, 'imdb_id': 'tt0499573'}, {'title': 'Strawberry Shortcake: Berry Big Help', 'year': 2014, 'imdb_id': 'tt3412692'}, {'title': "Super Monsters: Santa's Super Monster Helpers", 'year': 2020, 'imdb_id': 'tt13439998'}, {'title': "The Girl Can't Help It", 'year': 1956, 'imdb_id': 'tt0049263'}, {'title': 'The Help', 'year': 2011, 'imdb_id': 'tt1454029'}, {'title': 'The Helpers', 'year': 2012, 'imdb_id': 'tt1854582'}], 'search_results': 50, 'status': 'OK', 'status_message': 'Query was successful'}"""),
                  ("AbceXSADaf",   200,  "Sin resultados", "{'search_results': 0, 'status': 'OK', 'status_message': 'Query was successful'}"),
                  (" ",            200,  "Ingresa un nombre correctamente", """{'movie_results': [{'title': '!Women Art Revolution', 'year': 2010, 'imdb_id': 'tt1699720'}, {'title': '#1 Cheerleader Camp', 'year': 2010, 'imdb_id': 'tt1637976'}, {'title': '#AnneFrank. Parallel Stories', 'year': 2019, 'imdb_id': 'tt9850370'}, {'title': '#DanceBattle America', 'year': 0, 'imdb_id': 'tt5252186'}, {'title': '#Female Pleasure', 'year': 2018, 'imdb_id': 'tt8372826'}, {'title': '#FriendButMarried 2', 'year': 2020, 'imdb_id': 'tt11640412'}, {'title': '#IMomSoHard Live', 'year': 2019, 'imdb_id': 'tt10043726'}, {'title': '#Lucky Number', 'year': 2015, 'imdb_id': 'tt2538204'}, {'title': '#MeToo Wolf of Bollywood', 'year': 2019, 'imdb_id': 'tt12237986'}, {'title': '#Moscow on the Beach', 'year': 2018, 'imdb_id': 'tt9303508'}, {'title': '#UNFIT: The Psychology of Donald Trump', 'year': 2020, 'imdb_id': 'tt12304596'}, {'title': '#Walang Forever', 'year': 2015, 'imdb_id': 'tt5293858'}, {'title': '$5 a Day', 'year': 2008, 'imdb_id': 'tt1024733'}, {'title': '$50K and a Call Girl: A Love Story', 'year': 2014, 'imdb_id': 'tt2106284'}, {'title': '$elfie Shootout', 'year': 2016, 'imdb_id': 'tt4004608'}, {'title': "' AV muri' Fukada Nana 107 cmK kappu gingakei saikyo oppai muchakucha damashi momi", 'year': 2016, 'imdb_id': 'tt7476906'}, {'title': "'85: The Greatest Team in Pro Football History", 'year': 2016, 'imdb_id': 'tt4417402'}, {'title': "'Donnie Darko': Production Diary", 'year': 2004, 'imdb_id': 'tt0437161'}, {'title': "'Futurama': Welcome to the World of Tomorrow", 'year': 0, 'imdb_id': 'tt1223208'}, {'title': "'G' Men", 'year': 1935, 'imdb_id': 'tt0026393'}, {'title': "'Gator Bait", 'year': 1973, 'imdb_id': 'tt0074080'}, {'title': "'Harry Potter': Behind the Magic", 'year': 2005, 'imdb_id': 'tt0497106'}, {'title': "'Kutabare' Bocchan", 'year': 0, 'imdb_id': 'tt5821744'}, {'title': "'Master Harold'... and the Boys", 'year': 1985, 'imdb_id': 'tt0089564'}, {'title': "'Michael Winslow: Live' Featurette", 'year': 2002, 'imdb_id': 'tt1671444'}, {'title': "'n Saak van Geloof", 'year': 2011, 'imdb_id': 'tt2160051'}, {'title': "'Neath the Arizona Skies", 'year': 1934, 'imdb_id': 'tt0024805'}, {'title': "'Nicholas Nickleby': The Cast on the Cast", 'year': 2003, 'imdb_id': 'tt0778591'}, {'title': "'NYPD Blue': A Final Tribute", 'year': 0, 'imdb_id': 'tt0454761'}, {'title': "'Pimpernel' Smith", 'year': 1941, 'imdb_id': 'tt0034027'}, {'title': "'R Xmas", 'year': 2001, 'imdb_id': 'tt0217978'}, {'title': "'Til Lies Do Us Part", 'year': 2007, 'imdb_id': 'tt0958884'}, {'title': "'Tis the Season for Love", 'year': 2015, 'imdb_id': 'tt5056034'}, {'title': "'Twas the Night Before Bumpy", 'year': 1995, 'imdb_id': 'tt1443787'}, {'title': "'Twas the Night Before Christmas", 'year': 1974, 'imdb_id': 'tt0208654'}, {'title': "'Twas the Night", 'year': 2001, 'imdb_id': 'tt0282223'}, {'title': "'Weird Al' Yankovic - Live! The Alpocalypse Tour", 'year': 2011, 'imdb_id': 'tt1999811'}, {'title': '(500) Days of Summer', 'year': 2009, 'imdb_id': 'tt1022603'}, {'title': '(Astro) Turf Wars', 'year': 2010, 'imdb_id': 'tt1899098'}, {'title': '(Dis)Honesty: The Truth About Lies', 'year': 2015, 'imdb_id': 'tt2630898'}, {'title': '(My) Truth: The Rape of 2 Coreys', 'year': 2020, 'imdb_id': 'tt11835270'}, {'title': '(Romance) in the Digital Age', 'year': 2017, 'imdb_id': 'tt5525418'}, {'title': '(T)Raumschiff Surprise - Periode 1', 'year': 2004, 'imdb_id': 'tt0349047'}, {'title': '*batteries not included', 'year': 1987, 'imdb_id': 'tt0092494'}, {'title': "-about 'The White Bus'", 'year': 1968, 'imdb_id': 'tt0290396'}, {'title': '...All the Marbles', 'year': 1981, 'imdb_id': 'tt0081964'}, {'title': '...And Beautiful', 'year': 0, 'imdb_id': 'tt1198379'}, {'title': '...And Give Us Our Daily Sex', 'year': 1979, 'imdb_id': 'tt0079515'}, {'title': '...And Justice for All', 'year': 1979, 'imdb_id': 'tt0078718'}, {'title': '...And Miles to Go Before I Sleep.', 'year': 0, 'imdb_id': 'tt4155716'}], 'search_results': 50, 'status': 'OK', 'status_message': 'Query was successful'}"""),
                  ("&$%&/(",       403, "ERROR IN API CONNECTION", "ERROR IN API CONNECTION"))

         for inptt, estatus, val_esp, mock_json in cases:
             mockss.return_value.status_code = estatus
             mockss.return_value.json = mock_json
             fin_outpt = APIMovie().get_movie_titles(inptt)
             self.assertEqual(fin_outpt, val_esp)


    #test de integracion para la funcion "getMovie"
    def test_getMovie(self):

         cases = (("I Care a Lot", 
                     "tt9893250", 
                     "tt9893250",   
                     Movie("tt9893250","I Care a Lot", 2021, "A court-appointed legal guardian defrauds her older clients and traps them under her care. But her latest mark comes with some unexpected baggage.",
                                 "J Blakeson", "Rosamund Pike, Peter Dinklage, Eiza González, Dianne Wiest, Chris Messina, Isiah Whitlock Jr., Macon Blair, Alicia Witt, Damian Young, Nicolas Logan, Kevin McCormick, Michael Malvesti, Liz Eng",
                                             "Thriller, Drama, Comedy, Crime", "http://image.tmdb.org/t/p/original/gKnhEsjNefpKnUdAkn7INzIFLSu.jpg")),

                  ("Alien Contactee: A Conversation with Dr.Louis Turi", 
                   "tt12338276", 
                   "tt12338276",   
                   Movie("tt12338276","Alien Contactee: A Conversation with Dr.Louis Turi", 2020, 
                             "Contactees are people who have experienced contact with extraterrestrials. Dr. Louis Turi had four such encounters. This documentary exams his encounters, his relationship with Astrology, and how he has accurately predicted several major world events.ri",
                                 "Jeremy Norrie", "Louis Turi", "Documentary", "http://image.tmdb.org/t/p/original/xnwNfj7Og5GYy9IQ4vewohjGhTl.jpg")),
        
                   ("A Dark Matter",
                    "tt2386175",
                    "tt2386175",
                     Movie("tt2386175", "A Dark Matter", 2013, "Unhinged by his girlfriend's sudden departure, artist Angus begins slipping into a dark layer of reality ruled by a powerful demon. Believing that the key to finding her lies within, Angus plunges deeper into the infernal netherworld.",
                                                 "James Naylor", "Daniel Briere, Shauna Bradley, Ashiko Westguard, Troy Blundell, David Tompa, Danny Waugh, Marty Moreau, Walter Borden, Stephen G. Brown, Angela Froese, Roscoe van Dyke",
                                                     "Crime, Sci-Fi, Thriller", "http://image.tmdb.org/t/p/original/uTNwWSxdZDuOnWW0StuWxZvBtpj.jpg")),
                     ("A Passport to Hell",
                     "tt0023323",
                     "tt0023323",
                     Movie("tt0023323", "A Passport to Hell", 1932, "Just prior to the outbreak of World War I, in the British West African town of Akkra, English woman Myra Carson becomes involved in a scandal and is deported. While Myra's ship is docked at Duala, in German West Africa, the war breaks out and she finds herself facing internment by the Germans.",
                                                 "Frank Lloyd", "Elissa Landi, Paul Lukas, Warner Oland, Alexander Kirkland, Donald Crisp, Earle Foxe, Yola d'Avril, Ivan F. Simpson, Eva Dennison, Wilhelm von Brincken, Anders Van Haden, Bert Sprotte, John Lester Johnson, Vera Morrison, Herman Bing",
                                                     "Drama", "http://image.tmdb.org/t/p/original/5v7igvrxQvBaYTgGbCYWgj7IAqQ.jpg")) )
        
         for first, secnd, thrd, expected in cases:
             A = APIMovie().searchMovieTitle(first)
             B = APIMovie().searchMovieDetails(secnd)
             C = APIMovie().searchMovieImage(thrd)
             new_object_movie = Movie(A[0], A[1], A[2], B[0], B[1], B[2], B[3], C[0])
             self.assertEqual(str(new_object_movie), str(expected))
    


if __name__ == "__main__":
    unittest.main()