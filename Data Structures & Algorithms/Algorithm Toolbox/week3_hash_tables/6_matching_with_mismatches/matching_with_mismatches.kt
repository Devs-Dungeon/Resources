fun solve(k: Int, text: String, pattern: String): List<Int>  {
    val pos = ArrayList<Int>()
    return pos
}

fun main(args: Array<String>) {
    val inp = System.`in`.bufferedReader()
    val out = System.`out`.bufferedWriter()
    for (line in inp.readLines()) {
        val (k, s, t) = line.split(" ")
        val ans = solve(k.toInt(), s, t)
        out.write("${ans.size} ${ans.joinToString(" ")} \n");
    }
    out.close()
}
