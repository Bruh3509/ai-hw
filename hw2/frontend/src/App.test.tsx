import { render, screen, waitFor } from '@testing-library/react';
import { describe, it, expect, vi } from 'vitest';
import App from './App';
import * as api from './api/userApi';

// Mock the entire userApi module
vi.mock('./api/userApi');

const mockUsers = [
  { id: 1, name: 'Leanne Graham', username: 'Bret', email: 'Sincere@april.biz', phone: '1-770-736-8031 x56442', website: 'hildegard.org', company: { name: 'Romaguera-Crona', catchPhrase: 'Multi-layered client-server neural-net', bs: 'harness real-time e-markets' }, address: { street: 'Kulas Light', suite: 'Apt. 556', city: 'Gwenborough', zipcode: '92998-3874', geo: { lat: '-37.3159', lng: '81.1496' } } },
  { id: 2, name: 'Ervin Howell', username: 'Antonette', email: 'Shanna@melissa.tv', phone: '010-692-6593 x09125', website: 'anastasia.net', company: { name: 'Deckow-Crist', catchPhrase: 'Proactive didactic contingency', bs: 'synergize scalable supply-chains' }, address: { street: 'Victor Plains', suite: 'Suite 879', city: 'Wisokyburgh', zipcode: '90566-7771', geo: { lat: '-43.9509', lng: '-34.4618' } } }
];

describe('App Component', () => {
  it('should render the header', () => {
    (api.fetchUsers as vi.Mock).mockResolvedValue([]);
    render(<App />);
    expect(screen.getByText(/User Directory/i)).toBeInTheDocument();
  });

  it('should display loading message initially', () => {
    (api.fetchUsers as vi.Mock).mockResolvedValue([]);
    render(<App />);
    expect(screen.getByText(/Loading users.../i)).toBeInTheDocument();
  });

  it('should fetch and display users', async () => {
    (api.fetchUsers as vi.Mock).mockResolvedValue(mockUsers);
    render(<App />);

    await waitFor(() => {
      expect(screen.getByText('Leanne Graham')).toBeInTheDocument();
      expect(screen.getByText('Ervin Howell')).toBeInTheDocument();
    });

    expect(screen.queryByText(/Loading users.../i)).not.toBeInTheDocument();
  });
});
