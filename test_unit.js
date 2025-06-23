import react from 'react';
import { render, screen } from '@testing-library/react';
import MyComponent from './MyComponent';

test('renders app message', () => {
    render(<MyComponent />); 
    const linkELement = screen.getByText(/Fruit Management App/i/);
    expect(linkElement).toBeInTheDocument();


});


