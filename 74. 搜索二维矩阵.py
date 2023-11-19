class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        def bin_search(arr,target):
            l,r = 0,len(arr)-1
            while l <= r:
                mid = (l+r) // 2
                if arr[mid] == target:
                    return True
                elif arr[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return True if 0<= l <= len(arr)-1 and arr[l] == target else False
        M,N = len(matrix),len(matrix[0])
        for i in range(M):
            if bin_search(matrix[i],target) :
                return True
        return False

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        M,N = len(matrix),len(matrix[0])
        def get_idx(idx,matrix):
            M, N = len(matrix), len(matrix[0])
            # print(matrix)
            # print(idx,[idx // N],[idx - ((idx // N) * N)])
            return matrix[idx // N][idx - ((idx // N) * N)]
        l,r = 0, M*N-1
        while l<=r:
            mid = (l + r) // 2
            num = get_idx(mid,matrix)
            if num == target or get_idx(l,matrix) == target or get_idx(r,matrix) == target:
                return True
            elif num < target:
                l = mid + 1
            else:
                r = mid - 1
        return True if get_idx(r,matrix) == target else False