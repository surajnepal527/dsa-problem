/**
 * @return {Function}
 */
function createHelloWorld(){
    return function(...args){
        return "Hello World"
    }
}

createHelloWorld()
/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */