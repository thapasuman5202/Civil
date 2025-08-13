import { render, screen } from '@testing-library/react';
import { Hello } from './Hello';
import { describe, it, expect } from 'vitest';

describe('Hello component', () => {
  it('renders text', () => {
    render(<Hello />);
    expect(screen.getByText('Hello Component')).toBeTruthy();
  });
});
