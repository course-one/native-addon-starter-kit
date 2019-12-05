const assert = require( 'assert' );
const greet = require( '..' ); // loads ../index.js

describe( 'Test greet API', () => {
    it( 'should return `Hello Mike!`', () => {
        const result = greet.hello( 'Mike' ); // returns 'Hello Mike!'
        assert.equal( 'Hello Mike!', result );
    } );
} );
