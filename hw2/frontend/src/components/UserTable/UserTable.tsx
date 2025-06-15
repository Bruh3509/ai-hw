import React from 'react';
import { User } from '../../types/user';
import styles from './UserTable.module.css';

interface UserTableProps {
  users: User[];
  onSelectUser: (user: User) => void;
  onDeleteUser: (userId: number) => void;
}

const UserTable: React.FC<UserTableProps> = ({ users, onSelectUser, onDeleteUser }) => {
  return (
    <div className={styles.userTableContainer}>
      <div className={styles.headerRow}>
        <div className={styles.headerCell}>User</div>
        <div className={styles.headerCell}>Contact</div>
        <div className={styles.headerCell}>Company</div>
        <div className={styles.headerCell}>Actions</div>
      </div>
      {users.map((user) => (
        <div key={user.id} className={styles.userRow} data-testid={`user-row-${user.id}`}>
          <div className={styles.cell}>
            <div className={styles.userName}>{user.name}</div>
            <div className={styles.userEmail}>{user.email}</div>
          </div>
          <div className={styles.cell}>
            <div>{user.phone}</div>
            <a href={`http://${user.website}`} target="_blank" rel="noopener noreferrer" className={styles.websiteLink}>
              {user.website}
            </a>
          </div>
          <div className={styles.cell}>{user.company.name}</div>
          <div className={styles.cell}>
            <button className={styles.actionButton} onClick={() => onSelectUser(user)}>View</button>
            <button className={`${styles.actionButton} ${styles.deleteButton}`} onClick={() => onDeleteUser(user.id)}>Delete</button>
          </div>
        </div>
      ))}
    </div>
  );
};

export default UserTable;
