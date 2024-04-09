# The-Music-Club
# The-Music-Club

A music club asks its members upon joining to rank in order of preference,
 a fixed set of k classic song titles, with rank 1 being the most preferred title,
 and rank k being the member's least preferred. This preference ranking is called the member's preference profile. 
 Members are then allowed to listen to contemporary song titles in the club's library, and as they do so, 
 the club's music app automatically maintains a ranked list of their favourite song titles, called the member's top ranked list. 
 The library contains m song titles, each of which is given a unique index from 1 to m. Each top ranked list is a list of library indexes (which are independent of the indexes used for the preference profile). 
 The club owner wants to implement a feature that would recommend a song title from the top ranked lists of the members whose preference profiles are the nearest to that of the requestor.


He defines the distance between two preference profiles as the the number of times 
that they disagree on the relative ordering of a given pair of songs.

For example, suppose that Alice and Bob are members with the following preference profiles:

Alice: s_2, s_5, s_1, s_3, s4
Bob: S_3, s_4, s_2, s_1, s_5

Then this means that Alice likes Song #2 the most, and Song #4 the least, 
while Bob likes Song #3 the most and Song #5 the least. Observe that both prefer Song #2 over Song #5 (because each ranked Song #2 higher than Song #5), 
so they agree on the song pair (2, 5). But they disagree on the song pair (2, 3) because Alice likes Song #2 more than she does Song #3, while Bob does not. 
The song pairs that they disagree on are (2, 3), (2, 4), (1, 5), (3, 5), (4, 5), (1, 3), (1, 4), so the distance between their preference profiles is 7.

According to the club's owner, the best song to recommend to a member with preference profile P, and top ranked list T, is the highest ranked song, 
that is not already in T, taken from the top ranked lists of members whose preference distance from P is minimum. 
If there is more than one song with the same ranking that is not in T, 
then the song with the lowest index in the library should be recommended.

Given the preference profile and the top ranked list for each of n members, determine the best song to recommend to the first member of the list, 
and print its index in the library. If all the songs on the most similar club members' top ranked lists are already on the first member's list, then return -1.

Input Format

Line 1:k, r  The sizes of the preference profile and top ranked list
Line 2: n The number of club members
The next 2n lines are given as two lines for each index i: 1<=i<=n 
(a) k space separated values P_i1...P_ik indicating member i's preference profile, P.
(b) r space separated integers: T_i1...T_ir indicating member i's top ranked list, T_i.

Constraints

2<=k<=500
3<=r<=20
2<=n<=1000
100<=m<=10^9
1<=T_ij<=m

For each i, the sequence {P_i} will be a permutation of the values in the closed interval [1, k].

Output Format

A single integer indicating the index of the best song to recommend to the first member in the list, or -1 if none exists.

Sample Input 0

5 10
4
2 5 1 3 4
57 23 10 15 7 2 19 27 41 61
3 4 2 1 5
33 17 19 27 61 99 91 57 71 50
2 3 1 5 4
10 23 2 72 61 57 41 27 50 47
1 2 5 4 3
7 19 61 51 19 80 84 43 31 90
Sample Output 0

51


Explanation 0

The first member has a preference profile of 2,5,1,3,4 and a top 10 list of 57, 23, 10, 15, 7, 2, 19, 27, 41, 61.
The first two preference profiles are the same as the ones described in the example of the description. 
So, we know that the distance between the first two preference profiles is 7.

The distance between 2, 3, 1, 5, 4 and 2, 5, 1, 3, 4 is 3 (the disagreement pairs are (1, 3), (1, 5) and (3, 5)). 
The distance between 1, 2, 5, 4, 3 and 2, 5, 1, 3, 4 is also 3 (the disagreement pairs are (1, 2), (1, 5) and (3, 4)).

So members 3 and 4 are equally close to member 1. 
We examine the corresponding top 10 lists to find the highest ranked song index that is not already in the first member's top 10 list. 
For member 3, Song #72 is the highest ranked song not already in member 1's top 10 list, for member 4 it is Song #51. For each of them the rank of that song is 4, 
so we have a tie of recommendations for member 1 between Song #51 and Song #72. The tie breaker is the lower valued index, so we output 51 as the result.
