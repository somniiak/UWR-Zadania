function Foo() {
    function Qux() {
        console.log( "Foo::Qux")
    }

    this.Bar = function() {
        Qux();
    }
}

var foo = new Foo();
foo.Bar();
foo.Qux();