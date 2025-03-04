class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer[]
     */
    function twoSum($nums, $target) {
        $map = [];
        foreach ($nums as $index => $num) {
            $comp = $target - $num;
            if (isset($map[$comp])) {
                return [$map[$comp], $index];
            }
            $map[$num] = $index;
        }
        return [];
    }
}