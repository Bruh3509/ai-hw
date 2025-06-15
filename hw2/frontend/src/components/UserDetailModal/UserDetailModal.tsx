import React from 'react';
import { User } from '../../types/user';
import styles from './UserDetailModal.module.css';

interface UserDetailModalProps {
  user: User;
  onClose: () => void;
}

const UserDetailModal: React.FC<UserDetailModalProps> = ({ user, onClose }) => {
  const mapLink = `https://www.google.com/maps/search/?api=1&query=${user.address.geo.lat},${user.address.geo.lng}`;

  return (
    <div className={styles.modalOverlay} onClick={onClose}>
      <div className={styles.modalContent} onClick={(e) => e.stopPropagation()}>
        <button className={styles.closeButton} onClick={onClose}>×</button>
        <div className={styles.header}>
          <h2>{user.name}</h2>
          <p className={styles.username}>@{user.username}</p>
        </div>
        <div className={styles.detailsGrid}>
          <div className={styles.detailItem}>
            <label>Email</label>
            <p>{user.email}</p>
          </div>
          <div className={styles.detailItem}>
            <label>Phone</label>
            <p>{user.phone}</p>
          </div>
          <div className={styles.detailItem}>
            <label>Website</label>
            <a href={`http://${user.website}`} target="_blank" rel="noopener noreferrer">{user.website}</a>
          </div>
          <div className={styles.detailItem}>
            <label>Address</label>
            <p>{`${user.address.suite}, ${user.address.street}, ${user.address.city}, ${user.address.zipcode}`}</p>
            <a href={mapLink} target="_blank" rel="noopener noreferrer" className={styles.mapLink}>View on Map</a>
          </div>
          <div className={styles.detailItem}>
            <label>Company</label>
            <p>{user.company.name}</p>
            <p className={styles.catchPhrase}>"{user.company.catchPhrase}"</p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default UserDetailModal;
