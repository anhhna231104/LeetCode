class Solution {

    /**
     * @param String $s
     * @return Boolean
     */
    function isValid($s) {
        $brackets = [
            '('=>')',
            '{'=>'}',
            '['=>']'
        ];
        $parents = [];
        foreach(str_split($s) as $c){
            switch($c){
                case '(':
                case '{':
                case '[':
                    $parents[] = $c;
                    break;
                case ')':
                case '}':
                case ']':
                    if(!count($parents) || $c != $brackets[array_pop($parents)])
                        return false;
                default: break;
            }
        } 
        return count($parents)===0;        
    }
}