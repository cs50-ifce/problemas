import check50
import check50.c

@check50.check()
def exists():
    """O arquivo 'ola.c' existe."""
    check50.exists("ola.c")

@check50.check(exists)
def compiles():
    """O arquivo 'ola.c' compila."""
    check50.c.compile("ola.c", lcs50=True)

@check50.check(compiles)
def ana():
    """Responde corretamente ao nome Ana."""
    check50.run("./ola").stdin("Ana").stdout("Ana").exit()

@check50.check(compiles)
def bia():
    """Responde corretamente ao nome Bia."""
    check50.run("./ola").stdin("Bia").stdout("Bia").exit()

@check50.check(compiles)
def leo():
    """Responde corretamente ao nome Leo."""
    check50.run("./ola").stdin("Leo").stdout("Leo").exit()
