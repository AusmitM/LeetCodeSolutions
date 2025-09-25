class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        totalLen = len(nums1)+len(nums2)
        if totalLen%2 ==0:
            ind = int(totalLen/2)
            ind1 = 0
            ind2 = 0
            curr = 0
            prev = 0
            for i in range(ind+1):
                if ind1<len(nums1) and ind2<len(nums2):
                    if nums1[ind1]<nums2[ind2]:
                        prev = curr
                        curr = nums1[ind1]
                        ind1+=1
                    else:
                        prev = curr
                        curr = nums2[ind2]
                        ind2+=1
                elif ind1<len(nums1):
                    prev = curr
                    curr = nums1[ind1]
                    ind1+=1
                else:
                    prev = curr
                    curr = nums2[ind2]
                    ind2+=1
            return (prev+curr)/2
        else:
            ind = int(totalLen/2)
            ind1 = 0
            ind2 = 0
            curr = 0
            for i in range(ind+1):
                if ind1<len(nums1) and ind2<len(nums2):
                    if nums1[ind1]<nums2[ind2]:
                        curr = nums1[ind1]
                        ind1+=1
                    else:
                        curr = nums2[ind2]
                        ind2+=1
                elif ind1<len(nums1):
                    curr = nums1[ind1]
                    ind1+=1
                else:
                    curr = nums2[ind2]
                    ind2+=1
            return curr
