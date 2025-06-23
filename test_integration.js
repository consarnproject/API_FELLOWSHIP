describe('FastAPI and React Integration', () => {
    it('should list fruits fethed from FastAPI', () => {
        cy.visit('http://localhost:5173');
        cy.contains('fruit').should('be.visible');

    });

    it('should create a new fruit via the React form', () => {
        cy.visit('http://localhost:5173');
        cy.get('input[name="fruits"]').type('Cypress Item');
        cy.get('button[type="submit"]').click();
        cy.contains('Cypress Item').should('be.visible');
    });

});

