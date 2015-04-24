import fresh_tomatoes
import media

# Attributes of Movie Object: title, trailer_youtube_url, duration, storyline, poster_image_url, actor, director, data_release

Jaws = media.Movie("Jaws", "https://www.youtube.com/watch?v=3hIvvho2T1k",
							"2h 10m",
							"When a young woman is killed by a shark while skinny-dipping near the New England \
                            tourist town of Amity Island, police chief Martin Brody (Roy Scheider) wants to close \
                            the beaches, but mayor Larry Vaughn (Murray Hamilton) overrules him, fearing that the \
                            loss of tourist revenue will cripple the town. Ichthyologist Matt Hooper (Richard Dreyfuss) \
                            and grizzled ship captain Quint (Robert Shaw) offer to help Brody capture the killer beast, \
                            and the trio engage in an epic battle of man vs. nature.",
							"image/jaws.jpg",
							"Roy Scheider","Steven Spielberg","June 1, 1975 (USA)")
Saving_private_Ryan = media.Movie("Saving private Ryan", "https://www.youtube.com/watch?v=RYExstiQlLc",
							"2h 50m",
							"Captain John Miller (Tom Hanks) takes his men behind enemy lines to find Private James Ryan, \
                            whose three brothers have been killed in combat. Surrounded by the brutal realties of war, \
                            while searching for Ryan, each man embarks upon a personal journey and discovers their \
                            own strength to triumph over an uncertain future with honor, decency and courage",
							"image/savi.jpg",
							"Tom Hanks","Steven Spielberg","July 24, 1998 (USA)")
Jurassic_Park = media.Movie("Jurassic Park", "https://www.youtube.com/watch?v=RxrvaneULkE",
							"2h 7m",
							"In Steven Spielberg's massive blockbuster, paleontologists Alan Grant (Sam Neill) and \
                            Ellie Sattler (Laura Dern) and mathematician Ian Malcolm (Jeff Goldblum) are among \
                            a select group chosen to tour an island theme park populated by dinosaurs created from \
                            prehistoric DNA. While the park's mastermind, billionaire John Hammond (Richard Attenborough), \
                            assures everyone that the facility is safe, they find out otherwise when various ferocious \
                            predators break free and go on the hunt.",
							"image/jura.jpg",
							"Jeff Goldblum","Steven Spielberg","June 11, 1993 (USA)")
Lincoln = media.Movie("Lincoln", "https://www.youtube.com/watch?v=Xb_4O9bYNbI",
							"2h",
							"With the nation embroiled in still another year with the high death count of Civil War, \
                            President Abraham Lincoln (Daniel Day-Lewis) brings the full measure of his passion, \
                            humanity and political skill to what would become his defining legacy: to end the war \
                            and permanently abolish slavery through the 13th Amendment. Having great courage, acumen \
                            and moral fortitude, Lincoln pushes forward to compel the nation, and those in government \
                            who oppose him, to aim toward a greater good for all mankind.",
							"image/linc.jpg",
							"Daniel Day-Lewis","Steven Spielberg","November 9, 2012 (USA)")
Interstellar = media.Movie("Interstellar", "https://www.youtube.com/watch?v=0vxOhd4qlnA",
							"2h 49m",
							"In Earth's future, a global crop blight and second Dust Bowl are slowly rendering the planet \
                            uninhabitable. Professor Brand (Michael Caine), a brilliant NASA physicist, is working on plans \
                            to save mankind by transporting Earth's population to a new home via a wormhole. But first, \
                            Brand must send former NASA pilot Cooper (Matthew McConaughey) and a team of researchers through \
                            the wormhole and across the galaxy to find out which of three planets could be mankind's new home",
							"image/inte.jpg",
							"Matthew McConaughey","Christopher Nolan","November 5, 2014 (USA)")
Man_of_Steel = media.Movie("Man of Steel", "https://www.youtube.com/watch?v=Sqgv1Qz1at4",
							"2h 28m",
							"With the imminent destruction of Krypton, their home planet, Jor-El (Russell Crowe) and his wife \
                            seek to preserve their race by sending their infant son to Earth. The child's spacecraft lands at \
                            the farm of Jonathan (Kevin Costner) and Martha (Diane Lane) Kent, who name him Clark and raise \
                            him as their own son. Though his extraordinary abilities have led to the adult Clark (Henry Cavill) \
                            living on the fringe of society, he finds he must become a hero to save those he loves from a dire threat",
							"image/mano.jpg",
							"Henry Cavill","hristopher Nolan","June 14, 2013 (USA)")
The_Dark_Knight_Rises = media.Movie("The Dark Knight Rises", "https://www.youtube.com/watch?v=GokKUqLcvD8",
							"2h 45m",
							"It has been eight years since Batman (Christian Bale), in collusion with Commissioner Gordon \
                            (Gary Oldman), vanished into the night. Assuming responsibility for the death of Harvey Dent, \
                            Batman sacrificed everything for what he and Gordon hoped would be the greater good. However, \
                            the arrival of a cunning cat burglar (Anne Hathaway) and a merciless terrorist named Bane (Tom Hardy) \
                            force Batman out of exile and into a battle he may not be able to win",
							"image/thed.jpg",
							"Tom Hardy","Chritian Bale","July 20, 2012 (USA)")
Inception = media.Movie("Inception", "https://www.youtube.com/watch?v=8hP9D6kZseM",
							"2h 28m",
							"Dom Cobb (Leonardo DiCaprio) is a thief with the rare ability to enter people's dreams \
                            and steal their secrets from their subconscious. His skill has made him a hot commodity \
                            in the world of corporate espionage but has also cost him everything he loves. Cobb gets \
                            a chance at redemption when he is offered a seemingly impossible task: Plant an idea in \
                            someone's mind. If he succeeds, it will be the perfect crime, but a dangerous enemy \
                            anticipates Cobb's every move.",
							"",
							"Leonardo Dicarpio","Christopher Nolan","July 13, 2010 (USA)")
Schindler_list = media.Movie("Schindler's list", "https://www.youtube.com/watch?v=JdRGC-w9syA",
							"3h 15m",
							"Businessman Oskar Schindler (Liam Neeson) arrives in Krakow in 1939, ready to make his \
                            fortune from World War II, which has just started. When the SS begins exterminating Jews \
                            in the Krakow ghetto, Schindler arranges to have his workers protected to keep his factory \
                            in operation, but soon realizes that in so doing, he is also saving innocent lives",
							"image/schi.jpg",
							"Liam Neeson","Steven Spielberg","December 15, 1993 (USA)")

movies = [Schindler_list, Jurassic_Park, Jaws, Saving_private_Ryan, Lincoln, Interstellar, Man_of_Steel, 
            The_Dark_Knight_Rises, Inception]


# Attributes of Music Object: title, trailer_youtube_url, duration, author, performer, category

Nocturne_op_72 = media.Music("Nocturne op.72", "https://www.youtube.com/watch?v=vJpAIOFN5WQ",
								"4:44", "Fryderyk Chopin", "Artur Rubinstein", "instrumental")

Moonlight_Sotana = media.Music("Moonlight Sonata (full)", "https://www.youtube.com/watch?v=4Tr0otuiQuU",
								"15:00", "Ludwig van Bethoven", "Andrea Romano", "instrumental")

Nocturne_op_9_Number_2 = media.Music("Nocturne op.9 Number 2", "https://www.youtube.com/watch?v=9E6b3swbnWg",
								"4:29", "Fryderyk Chopin", "Andrea Romano", "instrumental")

Clair_de_Lune = media.Music("Clair de Lune", "https://www.youtube.com/watch?v=CvFH_6DNRCY",
								"5:00", "Claude Debussy", "Moura Lympany", "instrumental")

First_Arabesque = media.Music("First Arabesque", "https://www.youtube.com/watch?v=A6s49OKp6aE",
								"5:00", "Claude Debussy", "Stephen Malinowski", "instrumental")

Fantasy_in_D_minor_K397 = media.Music("Fantasy in D minor K397", "https://www.youtube.com/watch?v=OYiz_u0tDwM",
								"7:18", "Wolfgang Amadeus Mozart", "Mitsuko Uchida", "instrumental")

Turkish_March = media.Music("Turkish March", "https://www.youtube.com/watch?v=HMjQygwPI1c",
								"4:00", "Wolfgang Amadeus Mozart", "Ronald Brautigam", "instrumental")

Bad = media.Music("Bad", "https://www.youtube.com/watch?v=dsUXAEzaC3Q",
								"", "Michael Jackson", "Michael Jackson", "pop")

Smooth_Criminal = media.Music("Smooth Criminal", "https://www.youtube.com/watch?v=h_D3VFfhvs4",
								"", "Michael Jackson", "Michael Jackson", "pop")

Thriller = media.Music("Thriller", "https://www.youtube.com/watch?v=sOnqjkJTMaA",
								"", "Michael Jackson", "Michael Jackson", "pop")

Happy = media.Music("Happy", "https://www.youtube.com/watch?v=y6Sxv-sUYtM",
								"", "Pharrel Williams", "Pharrel Williams", "pop")

All_of_Me = media.Music("All of Me", "https://www.youtube.com/watch?v=450p7goxZqg",
								"", "John Legend", "John Legend", "pop")

Take_Me_To_Church = media.Music("Take Me To Church", "https://www.youtube.com/watch?v=MYSVMgRr6pw",
								"", "Hozier", "Hozier", "pop")

Titanium = media.Music("Titanium", "https://www.youtube.com/watch?v=JRfuAukYTKg",
								"", "David Guetta", "David Guetta ft. Sia", "pop")

We_Are_Young = media.Music("We Are Young", "https://www.youtube.com/watch?v=Sv6dMFF_yts",
								"", "Janelle Monae", "Janelle Monae", "pop")

All_of_me = media.Music("All of me", "https://www.youtube.com/watch?v=9fAZIQ-vpdw",
						"3:00", "Jon Schimdt","Jon Schimdt", "classical crossover")

Waterfall = media.Music("Waterfall", "https://www.youtube.com/watch?v=8P9hAN-teOU", 
						"3:30", "Jon Schimdt", "Jon Schimdt", "classical crossover")

Kungfu_Piano = media.Music("Kungfu Piano", "https://www.youtube.com/watch?v=NCaH-qqTWpk", 
						"4:25", "The Piano Guys", "The Piano Guys","classical crossover")

Batman_Evolution = media.Music("Batman Evolution", "https://www.youtube.com/watch?v=skVo8AYWRYk", 
								"6:20", "The Piano Guys", "The Piano Guys", "classical crossover")

Mission_Impossible = media.Music("Mission Impossible", "https://www.youtube.com/watch?v=9p0BqUcQ7i0", 
								"5:20", "The Piano Guys/Lindsey Stirling", "The Piano Guys/Lindsey Stirling", 
								"classical crossover")

The_Misssion = media.Music("The Misssion", "https://www.youtube.com/watch?v=CHV6BjuQOZQ", 
							"3:50", "The Piano Guys", "The Piano Guys", "classical crossover")

Crystallize = media.Music("Crystallize", "https://www.youtube.com/watch?v=aHjpOzsQ9YI", 
							"5:00", "Lindsey Stirling","Lindsey Stirling", "classical crossover")



musics = [Batman_Evolution, Crystallize, Bad, Smooth_Criminal, Nocturne_op_72, Moonlight_Sotana, 
            Nocturne_op_9_Number_2, Clair_de_Lune, First_Arabesque, Thriller, Happy, All_of_Me, 
            Take_Me_To_Church, Titanium, We_Are_Young, Fantasy_in_D_minor_K397, Turkish_March, 
            All_of_me, Waterfall, Kungfu_Piano,  Mission_Impossible, The_Misssion]


# Call the main function to make the index.html file and to open it

fresh_tomatoes.open_movies_page(movies, musics)


 
