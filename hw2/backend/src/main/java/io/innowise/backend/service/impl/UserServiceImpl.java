package io.innowise.backend.service.impl;

import io.innowise.backend.dto.CreateUserDto;
import io.innowise.backend.dto.UserDto;
import io.innowise.backend.entity.User;
import io.innowise.backend.repository.UserRepository;
import io.innowise.backend.service.UserService;
import lombok.RequiredArgsConstructor;
import org.modelmapper.ModelMapper;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;

@Service
@RequiredArgsConstructor
@Transactional(readOnly = true)
public class UserServiceImpl implements UserService {

    private final UserRepository userRepository;
    private final ModelMapper modelMapper;

    @Override
    public List<UserDto> findAll() {
        return userRepository.findAll().stream()
                .map(user -> modelMapper.map(user, UserDto.class))
                .collect(Collectors.toList());
    }

    @Override
    public Optional<UserDto> findById(Long id) {
        return userRepository.findById(id)
                .map(user -> modelMapper.map(user, UserDto.class));
    }

    @Override
    @Transactional
    public UserDto save(CreateUserDto createUserDto) {
        User user = modelMapper.map(createUserDto, User.class);
        User savedUser = userRepository.save(user);
        return modelMapper.map(savedUser, UserDto.class);
    }

    @Override
    @Transactional
    public Optional<UserDto> update(Long id, UserDto userDto) {
        return userRepository.findById(id)
                .map(existingUser -> {
                    // Map non-null properties from DTO to existing entity
                    modelMapper.map(userDto, existingUser);
                    existingUser.setId(id); // Ensure ID is not changed
                    User updatedUser = userRepository.save(existingUser);
                    return modelMapper.map(updatedUser, UserDto.class);
                });
    }

    @Override
    @Transactional
    public boolean deleteById(Long id) {
        if (userRepository.existsById(id)) {
            userRepository.deleteById(id);
            return true;
        }
        return false;
    }
}
