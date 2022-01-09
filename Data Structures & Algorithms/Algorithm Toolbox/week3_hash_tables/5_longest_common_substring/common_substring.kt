data class Answer(val i: Int, val j: Int, val len: Int)

fun solve(s: String, t: String): Answer {
    var ans = Answer(0, 0, 0)
    for (i in 0 until s.length)
        for (j in 0 until t.length)
            for (len in 0..minOf(s.length - i, t.length - j))
                if (len > ans.len && s.slice(i until i + len) == t.slice(j until j + len))
                    ans = Answer(i, j, len)
    return ans
}

fun main(args: Array<String>) {
    val inp = System.`in`.bufferedReader()
    val out = System.`out`.bufferedWriter()
    for (line in inp.readLines()) {
        val (s, t) = line.split(" ")
        val ans = solve(s, t)
        out.write("${ans.i} ${ans.j} ${ans.len}\n")
    }
    out.close()
}
