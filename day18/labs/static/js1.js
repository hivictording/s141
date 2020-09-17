function f(i) {
        var t = document.getElementById(i).innerText;
        var a = t.charAt(0);
        var b = t.substring(1,t.length);

        s = b;
        if (s.length == 0) {
           s = text;
        }
        document.getElementById(i).innerText = s;
    }

text = document.getElementById('center').innerText;

setInterval("f('center')",1000)