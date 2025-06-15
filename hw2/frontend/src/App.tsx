import React, { useState, useEffect } from 'react';
import { User } from './types/user';
import { fetchUsers } from './api/userApi';
import UserTable from './components/UserTable/UserTable';
import UserDetailModal from './components/UserDetailModal/UserDetailModal';
import './App.css';

const App: React.FC = () => {
  const [users, setUsers] = useState<User[]>([]);
  const [selectedUser, setSelectedUser] = useState<User | null>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const loadUsers = async () => {
      setLoading(true);
      try {
        const fetchedUsers = await fetchUsers();
        setUsers(fetchedUsers);
      } catch (err) {
        setError('Failed to load user data.');
      } finally {
        setLoading(false);
      }
    };
    loadUsers();
  }, []);

  const handleSelectUser = (user: User) => {
    setSelectedUser(user);
  };

  const handleCloseModal = () => {
    setSelectedUser(null);
  };

  const handleDeleteUser = (userId: number) => {
    setUsers(prevUsers => prevUsers.filter(user => user.id !== userId));
  };

  return (
    <div className="app">
      <header className="app-header">
        <h1>User Directory</h1>
        <p>A responsive directory of users from a test API.</p>
      </header>
      <main>
        {loading && <p className="loading-message">Loading users...</p>}
        {error && <p className="error-message">{error}</p>}
        {!loading && !error && (
          <UserTable
            users={users}
            onSelectUser={handleSelectUser}
            onDeleteUser={handleDeleteUser}
          />
        )}
      </main>
      {selectedUser && (
        <UserDetailModal user={selectedUser} onClose={handleCloseModal} />
      )}
    </div>
  );
};

export default App;
