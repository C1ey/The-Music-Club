import os
from operator import itemgetter

def merge_ordered_lists(list1, list2):
    index1 = 0
    index2 = 0
    count =  0
    merged_list = []
    while index1 < len(list1) and index2 < len(list2):
        if list1[index1] <= list2[index2]:
            merged_list.append(list1[index1])
            index1 += 1
        else:
            merged_list.append(list2[index2])
            index2 += 1
            count += len(list1) - index1
    merged_list += list1[index1:]
    merged_list += list2[index2:]
    return merged_list, count    

def count_songs(song_order):
    if len(song_order) <= 1:
        return song_order, 0
    midpoint = (len(song_order) // 2)
    left_list, left_count = count_songs(song_order[:midpoint])
    right_list, right_count = count_songs(song_order[midpoint:])
    merged_list, split_count = merge_ordered_lists(left_list, right_list)
    return merged_list, left_count + right_count + split_count

def measure_song_distance(member_profile1, member_profile2):
    profile2_song_rank = {song: i for i, song in enumerate(member_profile2)}
    profile1_song_rank = [profile2_song_rank[song] for song in member_profile1]
    null, count = count_songs(profile1_song_rank)
    return count

def suggest_best_song(group_members):
    primary_member_profile = group_members[0][0]
    primary_member_toplist = set(group_members[0][-1])
    closest_distance = float("inf")
    closest_members_indices = []
    for i in range(1, len(group_members)):
        current_distance = measure_song_distance(primary_member_profile, group_members[i][0])
        if current_distance < closest_distance:
            closest_distance = current_distance
            closest_members_indices = [i]
        elif current_distance == closest_distance:
            closest_members_indices.append(i)
    song_rank = {}
    for member_index in closest_members_indices:
        for rank, song in enumerate(group_members[member_index][1]):
            if song not in primary_member_toplist:
                if song not in song_rank or rank < song_rank[song]:
                    song_rank[song] = rank
    if not song_rank:
        return -1
    best_song, best_rank = min(song_rank.items(), key=itemgetter(1, 0))
    return best_song

if __name__ == "__main__":
    num_group_members, target_rank = map(int, input().split())
    num_songs = int(input())
    group_members = []
    for i in range(num_songs):
        member_profile = list(map(int, input().split()))
        top_song_list = list(map(int, input().split()))
        group_members.append((member_profile, top_song_list))
    recommended_song = suggest_best_song(group_members)
    print(recommended_song)
